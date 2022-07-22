from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, UpdateView
from inventory.models import Art
from .forms import SaleForm
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import reverse

from .models import SaleBill
from .utils.slack import slack_notify


class ArtListView(ListView):
    model = Art
    template_name = 'work_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ArtListView, self).get_context_data()
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context['pagelist'] = pagelist
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Art.objects.filter(
                Q(title__icontains=query) | Q(artist__icontains=query)
            )
        else:
            object_list = Art.objects.all()
        return object_list


class SaleView(View):
    template_name = 'work_detail.html'

    def get(self, request, pk):
        form = SaleForm(request.GET or None)
        art = Art.objects.filter(pk=pk)
        context = {
            'form': form,
            'art': art,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        model = SaleBill()

        purchaseQuantity = request.POST.get('purchaseQuantity')
        billNo = request.POST.get('billNo')
        walletAddr = request.POST.get('walletAddr')

        model.purchase_quantity = purchaseQuantity
        model.bill_no = billNo
        model.wallet_addr = walletAddr
        model.total_price = int(art.price) * int(purchaseQuantity)
        model.item_title = art.title
        model.art_id = art.art_id

        art.quantity -= int(model.purchase_quantity)

        art.save()
        model.save()

        sb_cnt = SaleBill.objects.all().count()
        sb_pending = SaleBill.objects.filter(is_send='pending').count()
        sb_success = SaleBill.objects.filter(is_send='success').count()

        slack_message = f"[전송 요청 등록] 작품명: {art.title}, 구매수량 - {model.purchase_quantity}\r\n요청 진행 중: {sb_pending}, 판매 완료: {sb_success}"
        slack_notify(slack_message, "#asyaaf-sale-bot-test", username="판매 알림봇")

        return HttpResponseRedirect(reverse('sale:bills'))

        # never use form before perfectly understand Django Forms

        # form = SaleForm(request.POST)
        #
        # if form.is_valid():
        #     bill = form.save(commit=False)
        #     bill.art_id = art.art_id
        #
        #     bill.item_title = art.title
        #
        #     art.quantity -= bill.purchase_quantity
        #
        #     bill.total_price = art.price * bill.purchase_quantity
        #
        #     art.save()
        #     bill.save()
        #     messages.success(request, "판매 요청이 성공적으로 완료되었습니다.")
        #     return redirect('sale:bills')
        # context = {
        #     'form': form,
        # }
        # return render(request, self.template_name, {'model': model})


class BillView(ListView):
    template_name = 'sale_list.html'
    model = SaleBill
    context_object_name = 'bills'
    ordering = ['-purchase_req_at']
    paginate_by = 10


class AdminListView(ListView):
    template_name = 'admin_list.html'
    model = SaleBill
    context_object_name = 'bills'
    ordering = ['-purchase_req_at']
    paginate_by = 10


class AdminUpdateView(UpdateView):
    template_name = 'admin_update.html'
    model = SaleBill
    fields = ['transaction_hash', 'is_send']
    success_url = '/transfer'