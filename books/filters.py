import django_filters
from django_filters import BooleanFilter, CharFilter

from books.models import Books


class BooksFilter(django_filters.FilterSet):
    is_active = BooleanFilter(field_name='is_active')
    genre = CharFilter(field_name='genre', lookup_expr='icontains')

    class Meta:
        model = Books
        fields = []
