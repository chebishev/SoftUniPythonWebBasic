from django import forms
from MyPlantApp.profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfile(ProfileForm):
    class Meta(ProfileForm.Meta):
        exclude = ['profile_picture']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }


class EditProfileForm(ProfileForm):
    class Meta(ProfileForm.Meta):
        labels = {

            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }