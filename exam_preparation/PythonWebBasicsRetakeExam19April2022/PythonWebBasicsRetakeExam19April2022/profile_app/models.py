from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_CHARACTERS = 30
    email = models.EmailField(
        blank=False,
        null=False
    )
    age = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(12),
        ]
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_CHARACTERS
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_CHARACTERS
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_CHARACTERS
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )
