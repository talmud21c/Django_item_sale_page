from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView
from inventory.models import Art
from .forms import SaleForm
from django.contrib import messages

from django.utils.decorators import method_decorator

from .models import SaleBill


class ArtListView(ListView):
    model = Art
    template_name = 'work_list.html'
    paginate_by = 5

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

        messages.success(request, "판매 요청이 성공적으로 완료되었습니다.")

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
        from django.http import HttpResponseRedirect
        from django.shortcuts import reverse

        return HttpResponseRedirect(reverse('sale:bills'))
        # return render(request, self.template_name, {'model': model})


class BillView(ListView):
    template_name = 'sale_list.html'
    model = SaleBill
    context_object_name = 'bills'
    ordering = ['-purchase_req_at']
    paginate_by = 10
