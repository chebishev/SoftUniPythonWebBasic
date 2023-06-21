from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class ProfileModel(models.Model):
    MAX_LENGTH = 30
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(12),
        ]
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LENGTH
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LENGTH,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LENGTH,
        verbose_name='Last Name'
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )
