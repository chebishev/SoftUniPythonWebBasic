from django import forms

from gamesPlay.game_app.models import GameModel


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'
