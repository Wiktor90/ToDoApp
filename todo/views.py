from django.shortcuts import render
from .models import Task

def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'todo/base.html', context)
