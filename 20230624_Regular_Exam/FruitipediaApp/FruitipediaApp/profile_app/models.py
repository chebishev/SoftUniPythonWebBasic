from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.profile_app.validators import name_starts_with_letter


# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[
            MinLengthValidator(2),
            name_starts_with_letter
        ]
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=[
            MinLengthValidator(1),
            name_starts_with_letter
        ]
    )
    email = models.EmailField(
        blank=False,
        null=False,
        max_length=40
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[
            MinLengthValidator(8)
        ]
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(
        default=18
    )
