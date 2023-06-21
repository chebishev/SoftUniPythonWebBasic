from django.shortcuts import render, redirect

from djangoProject.note_app.forms import NotesForm
from djangoProject.note_app.models import Note
from djangoProject.profile_app.forms import ProfileForm
from djangoProject.profile_app.models import Profile


# Create your views here.
def index(request):
    try:
        profile = Profile.objects.get()
    except Profile.DoesNotExist:
        profile = None

    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        form = ProfileForm()
        return render(request, 'home-no-profile.html', {'form': form})

    notes = Note.objects.all()
    return render(request, 'home-with-profile.html', {'notes': notes})


def add(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NotesForm()
    return render(request, 'note-create.html', {'form': form})


def edit(request, pk):
    current_note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=current_note)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NotesForm(instance=current_note)
    context = {
        'note': current_note,
        'form': form
    }
    return render(request, 'note-edit.html', context)


def delete(request, pk):
    note_to_delete = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note_to_delete.delete()
        return redirect('index')

    form = NotesForm(instance=note_to_delete)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
    context = {
        'note': note_to_delete,
        'form': form
    }
    return render(request, 'note-delete.html', context)


def details(request, pk):
    current_note = Note.objects.get(pk=pk)
    return render(request, 'note-details.html', {'note': current_note})
