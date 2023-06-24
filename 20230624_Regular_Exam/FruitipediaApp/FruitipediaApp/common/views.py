from django.shortcuts import render, redirect

from FruitipediaApp.fruit_app.models import FruitModel
from FruitipediaApp.profile_app.models import ProfileModel


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    profile = ProfileModel.objects.first()
    if not profile:
        return redirect('index')
    fruits = FruitModel.objects.all()
    return render(request, 'common/dashboard.html', {'fruits': fruits})
