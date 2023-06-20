from django.shortcuts import render

from gamesPlay.game_app.models import GameModel
from gamesPlay.profile_app.models import ProfileModel


# Create your views here.
def index(request):
    return render(request, 'home-page.html')


def dashboard(request):
    games = GameModel.objects.all()
    context = {
        'games': games
    }
    return render(request, 'dashboard.html', context)
