from django.urls import path, include
from .views import home_page, profile_details, profile_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path("profile/", include([
        path('', profile_details, name='profile details'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
]
