from django.core.validators import MinLengthValidator
from django.db import models
from musicApp.profile_app.validators import username_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), username_validator],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )