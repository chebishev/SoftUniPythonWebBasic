from django import forms

from PythonWebBasicsExam27February2022.album_app.models import Album


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        # removes the profile field from the form.
        # It is generated, because of the albums -> Profile relation
        exclude = ['profile']
        labels = {
            'album_name': 'Album Name',
            'image_url': 'Image URL',
        }


class CreateAlbumForm(BaseAlbumForm):
    class Meta(BaseAlbumForm.Meta):
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):
    pass
