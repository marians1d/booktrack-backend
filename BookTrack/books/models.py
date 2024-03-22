from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.DateField(null=True)
    isbn = models.CharField(max_length=20, null=True)
    page_count = models.IntegerField(null=True)
    cover_link = models.URLField(null=True)
    language = models.CharField(max_length=10)


