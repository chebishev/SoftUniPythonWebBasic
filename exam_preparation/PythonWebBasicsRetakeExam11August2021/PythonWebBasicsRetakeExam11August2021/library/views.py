from django.shortcuts import render, redirect

from PythonWebBasicsRetakeExam11August2021.library.forms import ProfileForm, BookForm
from PythonWebBasicsRetakeExam11August2021.library.models import Profile, Book


# Create your views here.
def index(request):
    try:
        get_profile = Profile.objects.get()
    except Profile.DoesNotExist:
        get_profile = None

    context = {
        'profile': get_profile,
        'books': Book.objects.all
    }
    if get_profile:
        return render(request, 'home-with-profile.html', context)

    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'home-with-profile.html', context)
        form = ProfileForm()
        return render(request, 'home-no-profile.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = BookForm()
    return render(request, 'add-book.html', {'form': form})


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = BookForm(instance=book)
    context = {
        'form': form,
        'book': book
    }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book-details.html', {'book': book})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')


def profile(request):
    return render(request, 'profile.html', {'profile': Profile.objects.first()})


def profile_edit(request):
    get_profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=get_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    form = ProfileForm(instance=get_profile)
    context = {
        'form': form,
        'profile': get_profile
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    get_profile = Profile.objects.first()
    books = Book.objects.all()
    if request.method == 'POST':
        get_profile.delete()
        books.delete()
        return redirect('index')

    form = ProfileForm(instance=get_profile)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)