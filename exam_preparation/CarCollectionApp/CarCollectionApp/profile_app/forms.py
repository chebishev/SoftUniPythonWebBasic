from django import forms

from CarCollectionApp.profile_app.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileCreateForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        exclude = ['first_name', 'last_name', 'profile_picture']


class ProfileEditForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }