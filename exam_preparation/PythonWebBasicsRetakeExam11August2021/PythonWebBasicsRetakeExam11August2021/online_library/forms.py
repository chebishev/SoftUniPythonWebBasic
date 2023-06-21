from django import forms

from PythonWebBasicsRetakeExam11August2021.online_library.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL',
        }


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'URL'}),
        }


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    pass


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['profile']


class CreateBookForm(BaseBookForm):
    class Meta(BaseBookForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime..'}),
        }


class EditBookForm(BaseBookForm):
    pass
