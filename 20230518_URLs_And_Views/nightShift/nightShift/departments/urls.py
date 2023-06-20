from django.urls import path
from nightShift.departments import views

urlpatterns = [
    path('', views.show_department),
    path('<int:department_id>/', views.test),
]
