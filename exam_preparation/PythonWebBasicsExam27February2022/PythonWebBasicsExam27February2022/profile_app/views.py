from django.shortcuts import render, redirect

from PythonWebBasicsExam27February2022.album_app.models import Album
from PythonWebBasicsExam27February2022.profile_app.forms import ProfileForm
from PythonWebBasicsExam27February2022.profile_app.models import Profile


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    if not profile:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home page')

        return render(request, 'home-no-profile.html', {'form': form})

    albums = Album.objects.all()
    return render(request, 'home-with-profile.html', {'albums': albums})


def profile_details(request):
    profile = Profile.objects.first()
    albums_count = Album.objects.all().count()
    return render(request, 'profile-details.html', {'profile': profile, 'albums_count': albums_count})


def profile_delete(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        # If you choose not to use the relationship between the Profile and the Album model
        # you need to delete the albums as well:
        # albums = Album.objects.all()
        # albums.delete()
        return redirect('home page')

    return render(request, 'profile-delete.html')