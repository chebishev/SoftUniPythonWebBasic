from django import forms

from PythonWebBasicsExam01November2020.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'title': 'Title',
            'image': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time (Minutes',
        }
