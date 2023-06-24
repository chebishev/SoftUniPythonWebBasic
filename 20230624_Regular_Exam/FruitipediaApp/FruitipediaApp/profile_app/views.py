from django.shortcuts import render, redirect

from FruitipediaApp.fruit_app.models import FruitModel
from FruitipediaApp.profile_app.forms import CreateProfileForm, EditProfileForm
from FruitipediaApp.profile_app.models import ProfileModel


# Create your views here.
def profile_create(request):
    profile = ProfileModel.objects.first()

    # just in case, in order to prevent second profile creation via direct url input
    if profile:
        return redirect('dashboard')
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'profile_app/create-profile.html', {'form': form})


def profile_details(request):
    fruits = FruitModel.objects.all()
    return render(request, 'profile_app/details-profile.html', {'fruits': fruits})


def profile_edit(request):
    form = EditProfileForm(request.POST or None, instance=ProfileModel.objects.first())
    if form.is_valid():
        form.save()
        return redirect('profile_details')

    return render(request, 'profile_app/edit-profile.html', {'form': form})


def profile_delete(request):
    profile = ProfileModel.objects.first()
    fruits = FruitModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')

    return render(request, 'profile_app/delete-profile.html')
