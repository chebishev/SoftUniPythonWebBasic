from django.contrib import admin

from PythonWebBasicsRetakeExam19April2022.game_app.models import Game


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'rating', 'max_level']

