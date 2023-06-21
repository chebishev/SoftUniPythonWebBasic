from django.shortcuts import render

from MyPlantApp.plant_app.models import PlantModel


# Create your views here.
def index(request):
    return render(request, 'home-page.html')


def catalogue(request):
    plants = PlantModel.objects.all()
    return render(request, 'catalogue.html', {'plants': plants})
