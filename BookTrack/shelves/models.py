from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Shelf(models.Model):
    name = models.CharField(max_length=50)

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
