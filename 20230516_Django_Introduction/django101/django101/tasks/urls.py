from django.urls import path
from django101.tasks import views

urlpatterns = [
    path('', views.index)
]