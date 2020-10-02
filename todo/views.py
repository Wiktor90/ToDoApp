from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, CreateAccount


def registerPage(request):
    form = CreateAccount()

    if request.method == 'POST':
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'todo/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'todo/login.html', context)

def logoutUser(request):
    context = {}
    return redirect(request, 'todo/login.html', context)

def tasks_list(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/base.html', context)

def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'todo/edit_task.html', {'form': form})

def delete_task (request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'todo/delete_task.html', {'task': task})