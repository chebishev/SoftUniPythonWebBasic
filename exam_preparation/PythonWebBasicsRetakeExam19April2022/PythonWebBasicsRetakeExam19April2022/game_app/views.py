from django.shortcuts import render, redirect

from PythonWebBasicsRetakeExam19April2022.game_app.forms import GameForm
from PythonWebBasicsRetakeExam19April2022.game_app.models import Game


# Create your views here.
def game_create(request):
    form = GameForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'game_app/create-game.html', {'form': form})


def game_details(request, id):
    game = Game.objects.get(id=id)
    return render(request, 'game_app/details-game.html', {'game': game})


def game_edit(request, id):
    game = Game.objects.get(id=id)
    form = GameForm(request.POST or None, instance=game)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }
    return render(request, 'game_app/edit-game.html', context)


def game_delete(request, id):
    game = Game.objects.get(id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')

    form = GameForm(instance=game)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'

    context = {
        'form': form,
        'game': game
    }
    return render(request, 'game_app/delete-game.html', context)
