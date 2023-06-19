from django.urls import path, include
from .views import index, \
    note_add, note_edit, note_delete, note_details, \
    profile, profile_delete

urlpatterns = [
    path('', index, name='index'),

    # notes urls
    path('add/', note_add, name='note_add'),
    path('edit/<int:pk>/', note_edit, name='note_edit'),
    path('delete/<int:pk>/', note_delete, name='note_delete'),
    path('details/<int:pk>/', note_details, name='note_details'),

    # profile urls
    path('profile/', include([
        path('', profile, name='profile'),
        path('delete/', profile_delete, name='profile_delete'),
    ])),
]
