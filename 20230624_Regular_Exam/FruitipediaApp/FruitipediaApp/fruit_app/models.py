from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruit_app.validators import name_only_letters


# Create your models here.
class FruitModel(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            name_only_letters
        ]
    )
    image_url = models.URLField(
        blank=False,
        null=False
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    nutrition = models.TextField(
        blank=True,
        null=True
    )
