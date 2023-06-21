from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def show_department(request):
    return HttpResponse("Hello, world. You're at the departments index.")


def test(request, department_id):
    department_name = ""
    if department_id == 1:
        department_name = "Developers"
    elif department_id == 2:
        department_name = "Trainers"
    html = "<html><body><h1><ul>" \
           "<li>Department Name: %s</li>" \
           "<br>  " \
           "<li>Department ID: %s</li></ul></h1></body></html>" \
           % (department_name, department_id)
    if department_name:
        return HttpResponse(html)
    else:
        return redirect("/")
