from django.urls import path
from .views import album_add, album_details, album_edit, album_delete

urlpatterns = [
    path('add/', album_add, name='add_album'),
    path('details/<int:pk>', album_details, name='details_album'),
    path('edit/<int:pk>', album_edit, name='edit_album'),
    path('delete/<int:pk>', album_delete, name='delete_album'),
]
