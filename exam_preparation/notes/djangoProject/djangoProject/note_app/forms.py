from django.forms import models

from djangoProject.note_app.models import Note


class NotesForm(models.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'image_url', 'content')

