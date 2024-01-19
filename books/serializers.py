from rest_framework import serializers

from books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
            'writer',
            'title',
            'published_date',
            'genre',
            'isbn',
            'price',
            'is_active',
            'is_deleted',
        ]
