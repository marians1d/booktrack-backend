from enum import Enum

from django.contrib.auth import models as auth_model
from django.core import validators
from django.db import models


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class BookTrackUser(auth_model.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH)]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH)]
    )

    email = models.EmailField(unique=True)

    gender = models.IntegerField(
        choices=Gender.choices(),
        default=Gender.OTHER.value
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.username

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        # Send email on successful register: Variant 2
        # Good enough, but there is a better option (signals)
        # send_mail....
        return result


