from django.shortcuts import render
from django.views.generic import View, CreateView, DetailView
from django_filters.views import FilterView
from inventory.models import Art
from .forms import SaleForm
from .models import SaleBill
from inventory.filters import ArtFilter


class ArtListView(FilterView):
    filterset_class = ArtFilter
    template_name = 'art_list.html'
    paginate_by = 10


class SaleView(View):
    template_name = 'sale_page.html'

    def get(self, request, pk):
        form = SaleForm(request.GET or None)
        item = Art.objects.filter(pk=pk)
        context = {
            'form': form,
            'item': item,
        }
        return render(request, self.template_name, context)

    def post(self, requset):
        form = SaleForm(requset.POST)
        if form.is_valid():
            sale_bill = form.save(commit=False)
            sale_bill.save()

            bill = SaleBill(id=id)
            bill.save()



        context = {

        }
        return render(requset, self.template_name, context)