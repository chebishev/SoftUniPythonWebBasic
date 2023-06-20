from django.shortcuts import render, redirect

from gamesPlay.game_app.forms import GameForm
from gamesPlay.game_app.models import GameModel


# Create your views here.
def create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = GameForm()
    context = {
        'form': form
    }
    return render(request, 'create-game.html', context)


def details(request, pk):
    game = GameModel.objects.get(id=pk)
    return render(request, 'details-game.html', {'game': game})


def edit(request, pk):
    game = GameModel.objects.get(id=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = GameForm(instance=game)
    context = {
        'form': form,
        'game': game

    }
    return render(request, 'edit-game.html', context)


def delete(request, pk):
    game = GameModel.objects.get(id=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')

    form = GameForm(instance=game)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    context = {
        'game': game,
        'form': form
    }
    return render(request, 'delete-game.html', context)
