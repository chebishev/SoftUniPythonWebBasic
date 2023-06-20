from django import forms
from .models import Profile
from .models import Book


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
