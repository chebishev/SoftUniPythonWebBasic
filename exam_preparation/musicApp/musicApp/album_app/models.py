from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Album(models.Model):
    MAX_LENGTH = 30
    album_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH,
        unique=True
    )
    artist = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH
    )
    genre = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH,
        choices=[
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ('R&B Music', 'R&B Music'),
            ('Rock Music', 'Rock Music'),
            ('Country Music', 'Country Music'),
            ('Dance Music', 'Dance Music'),
            ('Hip Hop Music', 'Hip Hop Music'),
            ('Other', 'Other')
        ]
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    image_url = models.URLField(
        null=True,
        blank=True
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0)
        ]
    )
