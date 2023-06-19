from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from CarCollectionApp.car_app.validators import year_validator


class CarModel(models.Model):
    CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")

    )

    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CHOICES
    )

    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)]
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[year_validator]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1)]
    )




