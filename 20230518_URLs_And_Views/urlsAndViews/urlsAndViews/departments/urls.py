from django.urls import path

from urlsAndViews.departments import views

urlpatterns = [
    path('department/', views.show_department),
    path('department/<department_id>/', views.show_department_by_id),
]
