from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtListView.as_view(), name='art'),
    path('new/', views.ArtCreateView.as_view(), name='new-art'),
    path('art/<pk>/edit', views.ArtUpdateView.as_view(), name='edit-art'),
    path('art/<pk>/delete', views.ArtDeleteView.as_view(), name='delete-art'),
]