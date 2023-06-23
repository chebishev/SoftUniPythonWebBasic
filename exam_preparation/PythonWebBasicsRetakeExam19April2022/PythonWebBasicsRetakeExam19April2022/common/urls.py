from django.urls import path
from .views import home_page, dashboard

urlpatterns = [
    path("", home_page, name="home page"),
    path("dashboard/", dashboard, name="dashboard"),
]
