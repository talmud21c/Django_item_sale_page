from django.urls import path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.ArtListView.as_view(), name='art'),
    path('sale/<int:pk>/', views.SaleView.as_view(), name='sale'),
    path('bills/', views.BillView.as_view(), name='bills'),
]