from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show_department(request):
    return HttpResponse("Hello, world. You're at the urlsAndViews department.")


def show_department_by_id(request, department_id):
    if department_id == 1:
        department_name = "Developers"
    elif department_id == 2:
        department_name = "Trainers"
    html = "<html><body><h1>" \
           "Department Name: %s, Department ID: %s" \
           "</h1></body></html>" \
           % (department_name, department_id)
    return HttpResponse(html)
