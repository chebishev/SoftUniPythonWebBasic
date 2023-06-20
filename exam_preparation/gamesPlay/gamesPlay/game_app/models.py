from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class GameModel(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        unique=True
    )
    category = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        choices=
        (
            ('Action', 'Action'),
            ('Adventure', 'Adventure'),
            ('Puzzle', 'Puzzle'),
            ('Strategy', 'Strategy'),
            ('Sports', 'Sports'),
            ('Board/Card Game', 'Board/Card Game'),
            ('Other', 'Other'),
        )
    )
    rating = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(5.0)
        ]
    )
    max_level = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1),
        ],
        verbose_name='Max Level'
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Image URL'
    )
    summary = models.TextField(
        blank=True,
        null=True
    )
