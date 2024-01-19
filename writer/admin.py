from django.contrib import admin
from django.utils import timezone

from writer.models import Writer


class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date', 'bio', 'is_active', 'is_deleted', 'created_at')
    list_filter = ('is_active', 'is_deleted', 'birth_date')
    search_fields = ['full_name']
    ordering = ['-id']
    list_per_page = 10

    fieldsets = (
        ('General Information', {
            'fields': ('full_name', 'birth_date', 'bio')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
    )

    actions = ['soft_delete']

    def soft_delete(self, request, queryset):
        queryset.update(is_deleted=True, is_active=False, deleted_at=timezone.now())

    soft_delete.short_description = "Seçilen yazarları yumuşak sil"


admin.site.register(Writer, WriterAdmin)
