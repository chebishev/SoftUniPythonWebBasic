from django.shortcuts import render, redirect

from examPreparation.recipes.forms import RecipeForm
from examPreparation.recipes.models import Recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()

    context = {
        "recipes": recipes
    }

    return render(request, "index.html", context)


def create(request):

    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = RecipeForm()
    context = {
        "form": form
    }

    return render(request, "create.html", context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = RecipeForm(instance=recipe)

    context = {
        "form": form,
        'recipe': recipe
    }

    return render(request, "edit.html", context)


def delete(request, pk):
    plant_to_delete = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        plant_to_delete.delete()

        return redirect("index")

    form = RecipeForm(instance=plant_to_delete)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'

    context = {
        "form": form,
        "plant_to_delete": plant_to_delete
    }
    return render(request, "delete.html", context)




def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    context = {
        "recipe": recipe,
        "ingredients": recipe.ingredients.split(", ")
    }
    return render(request, "details.html", context)
