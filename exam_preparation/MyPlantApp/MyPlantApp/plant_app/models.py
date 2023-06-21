from django.core.validators import MinLengthValidator
from django.db import models
from .validators import name_is_alpha


# Create your models here.
class PlantModel(models.Model):
    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=14,
        choices=[
            ("Outdoor Plants", "Outdoor Plants"),
            ("Indoor Plants", "Indoor Plants"),
        ],
        verbose_name='Type',
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[
            MinLengthValidator(2),
            name_is_alpha,
        ]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )
