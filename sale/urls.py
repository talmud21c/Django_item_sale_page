from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtListView.as_view(), name='art'),
    path('sale/<int:pk>/', views.SaleView.as_view(), name='sale'),
    # path('bills/', views.salebillview, name='bills'),
]