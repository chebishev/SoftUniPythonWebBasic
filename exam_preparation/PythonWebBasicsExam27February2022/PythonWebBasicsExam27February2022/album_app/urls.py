from django.urls import path
from .views import album_add, album_details, album_edit, album_delete

urlpatterns = [
    path('add/', album_add, name='album add'),
    path('details/<int:id>/', album_details, name='album details'),
    path('edit/<int:id>/', album_edit, name='album edit'),
    path('delete/<int:id>/', album_delete, name='album delete'),

]