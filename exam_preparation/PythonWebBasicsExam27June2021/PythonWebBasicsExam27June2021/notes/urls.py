from django.urls import path
from .views import index, add, edit, delete, details, profile, profile_delete

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('details/<int:pk>/', details, name='details'),
    path('profile/', profile, name='profile'),
    path('profile-delete/<int:pk>/', profile_delete, name='profile-delete'),
]
