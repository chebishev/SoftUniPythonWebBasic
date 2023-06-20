from django.shortcuts import render, redirect

from MyPlantApp.plant_app.models import PlantModel
from MyPlantApp.profile_app.forms import CreateProfile, EditProfileForm
from MyPlantApp.profile_app.models import Profile


def create_profile(request):
    form = CreateProfile(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    return render(request, 'create-profile.html', {'form': form})


def details_profile(request):
    total_stars = PlantModel.objects.all()[:3]

    context = {
        'total_stars': total_stars
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = CreateProfile(instance=profile)
    return render(request, 'edit-profile.html', {'form': form})


def delete_profile(request):
    profile = Profile.objects.first()
    plants = PlantModel.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('index')

    return render(request, 'delete-profile.html')


