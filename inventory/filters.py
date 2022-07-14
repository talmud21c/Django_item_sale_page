import django_filters
from .models import Art


class ArtFilter(django_filters.FilterSet):
    art_id = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Art
        fields = ['art_id']