from django.shortcuts import render, redirect

from CarCollectionApp.car_app.forms import CreatCar, EditCar, DeleteCar
from CarCollectionApp.car_app.models import CarModel


def create_car(request):

    form = CreatCar(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    return render(request, 'car-create.html', {'form': form})


def details_car(request, pk):
    car = CarModel.objects.get(pk=pk)

    return render(request, 'car-details.html', {'car': car})


def edit_car(request, pk):
    car = CarModel.objects.get(pk=pk)
    form = EditCar(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        'form': form,
        'car': car
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = CarModel.objects.get(pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = DeleteCar(instance=car)
    for f in form.fields.values():
        f.widget.attrs['disabled'] = True

    context = {
        'car': car,
        'form': form
    }

    return render(request, 'car-delete.html', context)
