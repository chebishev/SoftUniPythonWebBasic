from django import forms

from MyPlantApp.plant_app.models import PlantModel


class PlantForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'
