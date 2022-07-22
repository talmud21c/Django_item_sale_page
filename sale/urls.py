from django.urls import path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.ArtListView.as_view(), name='art'),
    path('sale/<slug:pk>/', views.SaleView.as_view(), name='sale'),
    path('bills/', views.BillView.as_view(), name='bills'),
    path('transfer/', views.AdminListView.as_view(), name='admin_list'),
    path('update/<slug:pk>', views.AdminUpdateView.as_view(), name='admin_update'),
]