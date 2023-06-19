from django.core.validators import MinValueValidator
from django.db import models
from .validators import username_min_length


# Create your models here.
class Profile(models.Model):
    MAX_LENGTH = 30  # just for password, first_name, last_name, because the value is the same for both
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=[
            username_min_length
        ]
    )
    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(18)
        ]
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )
