from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Shelf(models.Model):
    name = models.CharField(max_length=50)

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
