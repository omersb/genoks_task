from django.db import models
from django.utils import timezone

from books.models import Books


class Sales(models.Model):
    class Meta:
        db_table = 'sales'
        verbose_name = 'Sales'
        verbose_name_plural = 'Sales'
        ordering = ['-pk']

    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='sales')
    quantity = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} - {self.quantity}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def total_price(self):
        if self.book.price is not None:
            return self.book.price * self.quantity
        return 0  # price null ise 0 döndür
