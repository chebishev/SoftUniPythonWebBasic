from django.urls import path, include
from .views import index, add_book, edit_book, details_book, delete_book, profile, profile_edit, profile_delete

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>', edit_book, name='edit_book'),
    path('details/<int:pk>', details_book, name='details_book'),
    path('delete/<int:pk>', delete_book, name='delete_book'),
    path('profile/', include([
        path('', profile, name='profile'),
        path('edit/', profile_edit, name='profile_edit'),
        path('delete/', profile_delete, name='profile_delete'),
    ])),
]
