from django.contrib import admin

from PythonWebBasicsExam27June2021.notes.models import Profile, Note


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

