from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(unique=True, max_length=40, db_index=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    authors = models.CharField(max_length=100)
    categories = models.CharField(max_length=50, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True, db_index=True)
    page_count = models.IntegerField(blank=True, null=True)
    small_cover_link = models.URLField(blank=True, null=True)
    cover_link = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)


class UserBook(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    page_count = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
