from django.shortcuts import render, redirect
from musicApp.album_app.forms import AddAlbum, EditAlbum, DeleteAlbum
from musicApp.album_app.models import Album


# Create your views here.
def album_add(request):
    form = AddAlbum(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    return render(request, 'album-details.html', {'album': album})


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    form = EditAlbum(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('index')

    form = DeleteAlbum(instance=album)
    for f in form.fields.values():

        # Kak да забраним полетата 101
        # ЗАПОМНИ, ДЕСИ!!!
        f.widget.attrs['disabled'] = 'disabled'

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'delete-album.html', context)


