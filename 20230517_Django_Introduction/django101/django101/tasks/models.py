from django.db import models


# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_text = models.TextField()
    task_email = models.EmailField(default="")
    task_url = models.URLField(default="https://www.google.com")
    task_time = models.TimeField(default="00:00:00")
