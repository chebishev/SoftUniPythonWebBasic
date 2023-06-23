from django import forms

from PythonWebBasicsRetakeExam19April2022.game_app.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        labels = {
            'title': 'Title',
            'category': 'Category',
            'rating': 'Rating',
            'max_level': 'Max Level',
            'image_url': 'Image URL',
            'summary': 'Summary',
        }
