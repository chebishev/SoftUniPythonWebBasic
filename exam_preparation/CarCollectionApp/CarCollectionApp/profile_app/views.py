from django.shortcuts import render, redirect

from CarCollectionApp.car_app.models import CarModel
from CarCollectionApp.profile_app.forms import ProfileCreateForm, ProfileEditForm
from CarCollectionApp.profile_app.models import Profile


def get_profile():
    return Profile.objects.first()


# Create your views here.
def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    return render(request, 'profile-create.html', {'form': form})


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'profile-edit.html', {'form': form})


def profile_delete(request):
    profile = get_profile()
    cars = CarModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('index')

    return render(request, 'profile-delete.html')


def profile_details(request):
    profile = get_profile()
    if profile.first_name and profile.last_name:
        full_name = profile.first_name + ' ' + profile.last_name
    elif profile.first_name:
        full_name = profile.first_name
    else:
        full_name = profile.last_name
    cars = CarModel.objects.all()

    context = {
        'total_car_price': sum(car.price for car in cars),
        'full_name': full_name
    }
    return render(request, 'profile-details.html', context)
