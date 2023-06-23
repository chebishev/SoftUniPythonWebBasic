from django.contrib import admin

from PythonWebBasicsRetakeExam19April2022.profile_app.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'email']
