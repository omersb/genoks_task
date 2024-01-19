from django.contrib import admin
from django.utils import timezone

from books.models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_writer_full_name', 'title', 'published_date', 'genre', 'isbn', 'price', 'is_active',
                    'is_deleted']
    list_filter = ['is_active', 'is_deleted', 'created_at', 'updated_at', 'writer', 'genre']
    search_fields = ['title', 'genre', 'writer__full_name']
    ordering = ['-id']
    list_per_page = 10

    fieldsets = (
        ('General Information', {
            'fields': ('writer', 'title', 'published_date', 'genre', 'isbn', 'price')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
    )

    actions = ['soft_delete']

    def display_writer_full_name(self, obj):
        return obj.writer.full_name

    display_writer_full_name.short_description = 'Yazar'

    def soft_delete(self, request, queryset):
        queryset.update(is_deleted=True, is_active=False, deleted_at=timezone.now())

    soft_delete.short_description = "Seçilen yazarları yumuşak sil"


admin.site.register(Books, BooksAdmin)
