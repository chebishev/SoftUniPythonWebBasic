from django.urls import path
from .views import profile, delete

urlpatterns = [
    path('', profile, name='profile'),
    path('delete/<int:pk>/', delete, name='delete-profile'),
]
