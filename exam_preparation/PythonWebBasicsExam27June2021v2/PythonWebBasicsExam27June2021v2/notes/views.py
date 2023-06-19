from http.client import HTTPResponse

from django.shortcuts import render, redirect

from PythonWebBasicsExam27June2021v2.notes.forms import ProfileForm, NoteForm
from PythonWebBasicsExam27June2021v2.notes.models import Profile, Note


# Create your views here.
def index(request):
    get_profile = Profile.objects.first()
    notes = Note.objects.all()
    if not get_profile:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'home-no-profile.html', {'form': form})

    return render(request, 'home-with-profile.html', {'notes': notes})


def note_add(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'file': 'add_note'
    }
    return render(request, 'note-create.html', context)


def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-edit.html', context)


def note_delete(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('index')

    form = NoteForm(instance=note)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    context = {'note': note, 'form': form}

    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'note-details.html', {'note': note})


def profile(request):
    get_profile = Profile.objects.first()
    notes = Note.objects.all()
    context = {
        'notes': notes,
        'profile': get_profile,
    }
    return render(request, 'profile.html', context)


def profile_delete(request):
    get_profile = Profile.objects.first()
    notes = Note.objects.all()
    get_profile.delete()
    notes.delete()
    return redirect('index')
