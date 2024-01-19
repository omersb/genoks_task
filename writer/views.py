from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from utils.pagination import StandardPagination
from utils.swagger_doc import many_delete_swagger
from writer.filters import WriterFilter
from writer.models import Writer
from writer.serializers import WriterSerializer


class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    pagination_class = StandardPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = WriterFilter

    search_fields = ['full_name']
    ordering_fields = ['id', 'birth_date', 'is_active']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            # Superuser için tüm kayıtları döndür
            return Writer.objects.all()
        else:
            # Diğer kullanıcılar için sadece aktif ve silinmemiş kayıtları döndür
            return Writer.objects.filter(is_active=True, is_deleted=False)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

    def perform_destroy(self, instance):
        instance.delete()

    @many_delete_swagger
    @action(methods=['delete'], detail=False)
    def many_delete(self, request):
        ids = request.data.get('ids')
        if not isinstance(ids, list):
            return Response({'detail': 'Geçersiz veri biçimi: IDs bir liste olmalıdır.'},
                            status=status.HTTP_400_BAD_REQUEST)

        for writer in Writer.objects.filter(id__in=ids):
            writer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
