from django.db import models
from django.utils import timezone


class Writer(models.Model):
    class Meta:
        db_table = 'writer'
        verbose_name = 'Writer'
        verbose_name_plural = 'Writers'
        ordering = ['-pk']

    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    bio = models.TextField()

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
