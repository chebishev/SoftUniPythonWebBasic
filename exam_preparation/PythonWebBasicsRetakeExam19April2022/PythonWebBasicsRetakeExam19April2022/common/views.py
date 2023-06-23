from django.shortcuts import render, redirect

from PythonWebBasicsRetakeExam19April2022.game_app.models import Game
from PythonWebBasicsRetakeExam19April2022.profile_app.models import Profile


# Create your views here.
def home_page(request):
    return render(request, 'common/home-page.html')


def dashboard(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('home page')
    games = Game.objects.all().order_by('id')
    return render(request, 'common/dashboard.html', {'games': games})
