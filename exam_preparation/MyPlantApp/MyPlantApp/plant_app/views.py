from django.shortcuts import render, redirect
from MyPlantApp.plant_app.forms import PlantForm
from MyPlantApp.plant_app.models import PlantModel


def get_plant(plant_id):
    return PlantModel.objects.get(pk=plant_id)


# Create your views here.
def plant_create(request):
    form = PlantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    return render(request, 'create-plant.html', {'form': form})


def plant_details(request, pk):
    plant = get_plant(pk)
    return render(request, 'plant-details.html', {'plant': plant})


def plant_edit(request, pk):
    plant = get_plant(pk)
    form = PlantForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'plant': plant,
        'form': form
    }

    return render(request, 'edit-plant.html', context)


def plant_delete(request, pk):
    plant = get_plant(pk)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    form = PlantForm(instance=plant)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'delete-plant.html', context)
