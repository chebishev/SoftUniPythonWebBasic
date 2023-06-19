from django.contrib import admin

from examPreparation.recipes.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time')


# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
