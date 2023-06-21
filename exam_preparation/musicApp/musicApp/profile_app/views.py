from django.shortcuts import render, redirect
from musicApp.album_app.models import Album
from musicApp.profile_app.models import Profile


def profile_details(request):
    context = {
        'profile': Profile.objects.first(),
        'albums': Album.objects.all()
    }

    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('index')

    return render(request, 'profile-delete.html')


