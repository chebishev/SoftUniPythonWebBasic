from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Task


# Create your views here.
def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list
    }
    # output = "<li>"
    # output += "<li>".join(f"{t.task_title} - {t.task_text} - {t.task_hour}" for t in tasks_list)
    #
    # if not output:
    #     output = "There are no created tasks!"
    #
    # return HttpResponse(output)
    return render(request, 'task/index.html', context)
