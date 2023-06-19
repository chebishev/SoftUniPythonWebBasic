from django.db import models


# Create your models here.
class Profile(models.Model):
    NAME_MAX_LENGTH = 20
    first_name = models.CharField(max_length=NAME_MAX_LENGTH)
    last_name = models.CharField(max_length=NAME_MAX_LENGTH)
    age = models.PositiveIntegerField()
    image_url = models.URLField()


class Note(models.Model):
    TITLE_MAX_LENGTH = 30
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    image_url = models.URLField()
    content = models.TextField()
