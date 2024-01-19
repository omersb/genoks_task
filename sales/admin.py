from django.contrib import admin
from django.utils import timezone

from sales.models import Sales


class SalesAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_title', 'book_price', 'quantity', 'total_price', 'is_active', 'is_deleted',
                    'created_at', 'updated_at']
    list_filter = ['is_active', 'is_deleted', 'created_at', 'updated_at']
    search_fields = ['book__title']
    ordering = ['-id']
    list_per_page = 10

    fieldsets = (
        ('General Information', {
            'fields': ('book', 'quantity')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
    )

    actions = ['soft_delete']

    def book_title(self, obj):
        return obj.book.title

    book_title.short_description = 'Kitap Adı'

    def book_price(self, obj):
        return obj.book.price

    book_price.short_description = 'Kitap Adet Fiyatı'

    def soft_delete(self, request, queryset):
        queryset.update(is_deleted=True, is_active=False, deleted_at=timezone.now())

    soft_delete.short_description = "Seçilen satışları yumuşak sil"

    def total_price(self, obj):
        return obj.total_price()

    total_price.short_description = 'Toplam Fiyat'


admin.site.register(Sales, SalesAdmin)
