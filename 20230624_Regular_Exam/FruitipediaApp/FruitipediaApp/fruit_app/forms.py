from django import forms

from FruitipediaApp.fruit_app.models import FruitModel


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class CreateFruitForm(BaseFruitForm):
    class Meta(BaseFruitForm.Meta):
        labels = {
            'name': False,
            'description': False,
            'image_url': False,
            'nutrition': False
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class EditFruitForm(BaseFruitForm):
    class Meta(BaseFruitForm.Meta):
        labels = {
            'image_url': 'Image URL',
        }


class DeleteFruitForm(BaseFruitForm):
    class Meta(BaseFruitForm.Meta):
        exclude = ['nutrition']
        labels = {
            'image_url': 'Image URL',
        }