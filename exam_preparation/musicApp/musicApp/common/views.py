from django.shortcuts import render, redirect

from musicApp.album_app.models import Album
from musicApp.profile_app.forms import ProfileForm
from musicApp.profile_app.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.first()
    if not profile:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'home-no-profile.html', {'form': form})

    return render(request, 'home-with-profile.html', {'albums': Album.objects.all()})
