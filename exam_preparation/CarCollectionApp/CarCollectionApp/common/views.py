from django.shortcuts import render

from CarCollectionApp.car_app.models import CarModel


# Create your views here.
def index(request):
    return render(request, 'index.html')


def catalogue(request):
    cars = CarModel.objects.all()
    return render(request, 'catalogue.html', {'cars': cars})
