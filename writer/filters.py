import django_filters
from django_filters import BooleanFilter

from writer.models import Writer


class WriterFilter(django_filters.FilterSet):
    is_active = BooleanFilter(field_name='is_active')

    class Meta:
        model = Writer
        fields = []
