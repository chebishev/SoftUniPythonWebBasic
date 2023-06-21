from django.shortcuts import render, redirect

from gamesPlay.game_app.models import GameModel
from gamesPlay.profile_app.forms import CreateProfileForm, EditProfileForm
from gamesPlay.profile_app.models import ProfileModel


# Create your views here.
def create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def details(request):
    profile = ProfileModel.objects.first()
    if profile.first_name and profile.last_name:
        full_name = profile.first_name + ' ' + profile.last_name

    elif profile.first_name or profile.last_name:
        full_name = profile.first_name if profile.first_name else profile.last_name

    else:
        full_name = None
    games = GameModel.objects.all()
    number_of_games = len(games)
    average_rating = 0.0 if not games else sum([game.rating for game in games]) / len(games)
    context = {
        'profile': profile,
        'full_name': full_name,
        'number_of_games': number_of_games,
        'average_rating': average_rating
    }
    return render(request, 'details-profile.html', context)


def edit(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    form = EditProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def delete(request):
    profile = ProfileModel.objects.first()
    games = GameModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('index')

    return render(request, 'delete-profile.html')
