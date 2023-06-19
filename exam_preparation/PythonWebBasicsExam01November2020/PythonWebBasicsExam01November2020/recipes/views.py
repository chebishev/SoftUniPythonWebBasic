from django.shortcuts import render, redirect

from PythonWebBasicsExam01November2020.recipes.forms import RecipeForm
from PythonWebBasicsExam01November2020.recipes.models import Recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def create(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'create.html', {'form': form})


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')

    form = RecipeForm(instance=recipe)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'details.html', context)
