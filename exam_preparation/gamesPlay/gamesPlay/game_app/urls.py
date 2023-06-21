from django.urls import path
from .views import create, details, edit, delete

urlpatterns = [
    path('create/', create, name='create_game'),
    path('details/<int:pk>/', details, name='details_game'),
    path('edit/<int:pk>/', edit, name='edit_game'),
    path('delete/<int:pk>/', delete, name='delete_game'),
]
