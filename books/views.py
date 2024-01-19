from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from books.filters import BooksFilter
from books.models import Books
from books.serializers import BooksSerializer
from utils.pagination import StandardPagination
from utils.swagger_doc import many_delete_swagger


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = StandardPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BooksFilter

    search_fields = ['title', 'genre', 'writer__full_name']
    ordering_fields = ['id', 'price', 'published_date', 'is_active']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            # Superuser için tüm kayıtları döndür
            return Books.objects.all()
        else:
            # Diğer kullanıcılar için sadece aktif ve silinmemiş kayıtları döndür
            return Books.objects.filter(is_active=True, is_deleted=False)

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

        for books in Books.objects.filter(id__in=ids):
            books.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
