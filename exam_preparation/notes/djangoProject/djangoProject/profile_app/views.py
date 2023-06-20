from django.shortcuts import render, redirect

from djangoProject.note_app.models import Note
from djangoProject.profile_app.models import Profile


# Create your views here.
def profile(request):
    current_profile = Profile.objects.first()
    number_of_notes = len(Note.objects.all())
    context = {
        'profile': current_profile,
        'number_of_notes': number_of_notes
    }
    return render(request, 'profile.html', context)


def delete(request, pk):
    profile_to_delete = Profile.objects.get(pk=pk)
    notes = Note.objects.all()
    profile_to_delete.delete()
    notes.delete()
    return redirect('index')