from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Z0-9_]*$',
                message="Ensure this value contains only letters, numbers, and underscore.",
            )
        ],
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
