from django import forms

from PythonWebBasicsExam27June2021v2.notes.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': "Link to Profile Image"
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': "Link to Image"
        }
