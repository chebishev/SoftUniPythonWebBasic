from django.shortcuts import render, redirect

from PythonWebBasicsExam27June2021.notes.forms import ProfileForm, NoteForm
from PythonWebBasicsExam27June2021.notes.models import Profile, Note


def get_profile():
    try:
        profile_obj = Profile.objects.get()
        return profile_obj
    except Profile.DoesNotExist:
        return


# Create your views here.
def index(request):
    if get_profile():
        context = {
            'profile': get_profile(),
            'notes': Note.objects.all()
        }
        return render(request, 'home-with-profile.html', context)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home-with-profile.html')

    form = ProfileForm()
    context = {
        'form': form,
        'file': 'home-no-profile'
    }
    return render(request, 'home-no-profile.html', context)


def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NoteForm()
    context = {
        'form': form,
        'file': 'note-create'
    }
    return render(request, 'note-create.html', context)


def edit(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NoteForm(instance=note)
    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-edit.html', context)

def delete(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('index')

    form = NoteForm(instance=note)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    context = {
        'form': form,
        'note': note
    }
    return render(request, 'note-delete.html', context)
def details(request, pk):
    note = Note.objects.get(id=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)

def profile(request):
    profile_info = get_profile()
    notes = Note.objects.all()
    context = {
        'profile': profile_info,
        'notes': notes
    }
    return render(request, 'profile.html', context)

def profile_delete(request, pk):
    profile_to_delete = Profile.objects.get(id=pk)
    profile_to_delete.delete()
    Note.objects.all().delete()
    return redirect('index')