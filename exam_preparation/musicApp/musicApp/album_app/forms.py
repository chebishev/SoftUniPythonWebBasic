from django import forms
from musicApp.album_app.models import Album


class AlbumBase(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image_url': 'Image URL',
            'price': 'Price'
        }


class AddAlbum(AlbumBase):
    # required for working labels and widgets
    class Meta(AlbumBase.Meta):

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class EditAlbum(AlbumBase):
    pass


class DeleteAlbum(AlbumBase):
    pass



