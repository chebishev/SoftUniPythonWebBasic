from django import forms
from django.forms import models

from djangoProject.profile_app.models import Profile


class ProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
