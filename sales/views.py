from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from sales.models import Sales
from sales.serializers import SalesSerializer
from utils.pagination import StandardPagination


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    pagination_class = StandardPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ['book__title', 'book__genre', 'book__writer__full_name']
    ordering_fields = ['id', 'quantity', 'created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            # Superuser için tüm kayıtları döndür
            return Sales.objects.all()
        else:
            # Diğer kullanıcılar için sadece aktif ve silinmemiş kayıtları döndür
            return Sales.objects.filter(is_active=True, is_deleted=False)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

    def perform_destroy(self, instance):
        instance.delete()
