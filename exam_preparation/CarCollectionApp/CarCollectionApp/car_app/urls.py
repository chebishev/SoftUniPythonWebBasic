from django.urls import path
from CarCollectionApp.car_app import views

urlpatterns = [
    path('create/', views.create_car, name='create car'),
    path('<int:pk>/details/', views.details_car, name='details car'),
    path('<int:pk>/edit/', views.edit_car, name='edit car'),
    path('<int:pk>/delete/', views.delete_car, name='delete car'),
]
