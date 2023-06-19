from django.urls import path
from .views import profile_create, profile_edit, profile_delete, profile_details

urlpatterns = [
    path('create/', profile_create, name='profile_create'),
    path('edit/', profile_edit, name='profile_edit'),
    path('delete/', profile_delete, name='profile_delete'),
    path('details/', profile_details, name='profile_details'),
]