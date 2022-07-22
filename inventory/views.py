from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Art
from .forms import ArtForm
from django_filters.views import FilterView
from .filters import ArtFilter


# 재고 표시 뷰
class ArtListView(FilterView):
    template_name = 'inventory_list.html'
    paginate_by = 10
    filterset_class = ArtFilter


# 작품 등록 뷰
class ArtCreateView(SuccessMessageMixin, CreateView):
    model = Art
    form_class = ArtForm
    template_name = "edit_art.html"
    success_url = '/art'
    success_message = "작품이 성공적으로 저장되었습니다"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = '작품 등록'
        context["savebtn"] = '저장하기'
        return context

    def get_success_url(self):
        return reverse('inventory_list')


# 작품 수정 뷰
class ArtUpdateView(SuccessMessageMixin, UpdateView):
    model = Art
    form_class = ArtForm
    template_name = "edit_art.html"
    success_url = '/art'
    success_message = "작품이 성공적으로 수정되었습니다"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = '작품 수정'
        context["savebtn"] = '저장하기'
        context["delbtn"] = '삭제하기'
        return context


# 작품 삭제 뷰
class ArtDeleteView(View):
    template_name = "delete_art.html"
    success_message = "Stock has been deleted successfully"

    def get(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        return render(request, self.template_name, {'art': art})

    def post(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        art.delete()
        messages.success(request, self.success_message)
        return redirect('/inventory')