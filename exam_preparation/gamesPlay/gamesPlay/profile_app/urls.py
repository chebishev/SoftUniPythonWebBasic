from django.urls import path
from .views import create, details, edit, delete

urlpatterns = [
    path('create/', create, name='profile_create'),
    path('details/', details, name='profile_details'),
    path('edit/', edit, name='profile_edit'),
    path('delete/', delete, name='profile_delete'),
]
