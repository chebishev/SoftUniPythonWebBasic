from django import forms

from gamesPlay.profile_app.models import ProfileModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = ProfileModel
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('email', 'age', 'password')


class EditProfileForm(BaseProfileForm):
    pass
