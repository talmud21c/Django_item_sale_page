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


class BillCreateView(CreateView):
    # 페이지 로드하면서 상세페이지 + 수정페이지
    # GET 요청 시 상세페이지 + 입력칸
    # 지갑 주소, 영수증 번호 입력 후 저장 버튼 누르면
    # 구매 목록에 작품ID + 구매 내역 save()

    model = SaleBill
    template_name = 'sale.html'
    form_class = SaleForm

#     def get(self, request):
#         model = Art
#         form = SaleForm(request.GET or None)
#         arts = Art.objects.filter()
#         pass
#     def post(self, request):
#         pass
#
#
# def detailview(request, pk):
#     if request.method == 'GET':
#         model = Art
#
#     else:
#     pass
#
#
# def salebillview(request):
#     pass