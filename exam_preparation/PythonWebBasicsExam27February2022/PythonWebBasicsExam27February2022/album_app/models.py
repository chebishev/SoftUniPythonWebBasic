from django.core.validators import MinValueValidator
from django.db import models

from PythonWebBasicsExam27February2022.profile_app.models import Profile


# Create your models here.
class Album(models.Model):
    MAX_LENGTH = 30
    album_name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=MAX_LENGTH
    )
    artist = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LENGTH
    )
    genre = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LENGTH,
        choices=(
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ("R&B Music", "R&B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music", "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip-Hop Music", "Hip-Hop Music"),
            ("Other", "Other"),
        )
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    image_url = models.URLField(
        blank=False,
        null=False
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0)]
    )
    # This makes a connection to the Profile model.
    # When the profile model is deleted, all the albums will be deleted too.
    # Comment it if you don't want to use it.
    # I'll provide the solution without this line in the album_app and profile_app views.
    # album_add view and profile_delete view
    profile = models.ForeignKey(
        to=Profile, on_delete=models.CASCADE
    )

