from django.urls import path, include
from .views import index, \
    book_add, book_edit, book_details, book_delete, \
    profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', index, name='index'),

    path('add/', book_add, name='book_add'),
    path('edit/<int:id>/', book_edit, name='book_edit'),
    path('details/<int:id>/', book_details, name='book_details'),
    path('delete/<int:id>/', book_delete, name='book_delete'),

    path("profile/", include([
        path('', profile_details, name='profile_details'),
        path('edit/', profile_edit, name='profile_edit'),
        path('delete/', profile_delete, name='profile_delete'),
    ]))
]
