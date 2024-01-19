from django.db import models
from django.utils import timezone

from writer.models import Writer


class Books(models.Model):
    class Meta:
        db_table = 'books'
        verbose_name = 'Books'
        verbose_name_plural = 'Books'
        ordering = ['-pk']

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='books')

    title = models.CharField(max_length=255)
    published_date = models.DateField()
    genre = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.writer} - {self.title}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
