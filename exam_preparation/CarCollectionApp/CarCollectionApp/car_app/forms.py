from django import forms
from CarCollectionApp.car_app.models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }


class CreatCar(CarForm):
    pass


class EditCar(CarForm):
    pass


class DeleteCar(CarForm):
    pass
