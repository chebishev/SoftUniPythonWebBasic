from django import forms
from PythonWebBasicsExam27June2021.notes.models import Profile, Note

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
