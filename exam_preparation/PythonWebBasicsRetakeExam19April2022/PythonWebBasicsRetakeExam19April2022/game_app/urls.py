from django.urls import path
from .views import game_create, game_details, game_edit, game_delete

urlpatterns = [
    path('create/', game_create, name='game create'),
    path('details/<int:id>/', game_details, name='game details'),
    path('edit/<int:id>/', game_edit, name='game edit'),
    path('delete/<int:id>/', game_delete, name='game delete'),
]