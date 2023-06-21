from django.shortcuts import render, redirect

from PythonWebBasicsRetakeExam11August2021.online_library.forms import CreateProfileForm, CreateBookForm, EditBookForm, \
    EditProfileForm, DeleteProfileForm
from PythonWebBasicsRetakeExam11August2021.online_library.models import Profile, Book


# Create your views here.
def index(request):
    profile = Profile.objects.first()

    if not profile:

        form = CreateProfileForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('index')

        return render(request, 'home-no-profile.html', {'form': form})

    books = Book.objects.all()
    return render(request, 'home-with-profile.html', {'books': books})


def book_add(request):
    profile = Profile.objects.first()
    form = CreateBookForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.profile = profile
            form.save()
            return redirect('index')

    return render(request, 'add-book.html', {'form': form})


def book_edit(request, id):
    book = Book.objects.get(id=id)
    form = EditBookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book
    }
    return render(request, 'edit-book.html', context)


def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book-details.html', {'book': book})


def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('index')


def profile_details(request):
    return render(request, 'profile.html')


def profile_edit(request):
    form = EditProfileForm(request.POST or None, instance=Profile.objects.first())
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'edit-profile.html', {'form': form})


def profile_delete(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'

    return render(request, 'delete-profile.html', {'form': form})
