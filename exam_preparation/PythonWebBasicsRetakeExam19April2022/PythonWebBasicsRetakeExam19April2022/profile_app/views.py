from django.shortcuts import render, redirect

from PythonWebBasicsRetakeExam19April2022.game_app.models import Game
from PythonWebBasicsRetakeExam19April2022.profile_app.forms import CreateProfileForm, EditProfileForm
from PythonWebBasicsRetakeExam19April2022.profile_app.models import Profile


# Create your views here.
def profile_create(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home page')

    return render(request, 'profile_app/create-profile.html', {'form': form})


def profile_details(request):
    profile = Profile.objects.first()
    profile_full_name = f"{profile.first_name} {profile.last_name}".replace('None', '')
    games = Game.objects.all()
    average_rating = 0 if not games else sum([game.rating for game in games]) / len(games)
    context = {
        'profile_full_name': profile_full_name,
        "games": games,
        "average_rating": average_rating
    }
    return render(request, 'profile_app/details-profile.html', context)


def profile_edit(request):
    form = EditProfileForm(request.POST or None, instance=Profile.objects.first())
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile details')

    return render(request, 'profile_app/edit-profile.html', {'form': form})


def profile_delete(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        Game.objects.all().delete()
        return redirect('home page')

    return render(request, 'profile_app/delete-profile.html')
