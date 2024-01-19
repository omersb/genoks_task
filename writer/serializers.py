from rest_framework import serializers

from books.serializers import BooksSerializer
from writer.models import Writer


class WriterSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = [
            'id',
            'full_name',
            'birth_date',
            'bio',
            'books',
            'is_active',
            'is_deleted',
        ]
