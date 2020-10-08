from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, CreateAccount
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated == False:
        form = CreateAccount()
        if request.method == 'POST':
            form = CreateAccount(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, '{} - Account successfully created. Please Log In.'.format(user), extra_tags='created')
                return redirect('login')
            else:
                messages.error(request, "Username is owned or Password don't match!")

        context = {'form': form}
        return render(request, 'todo/register.html', context)

    else:
        return redirect('tasks_list')

def loginPage(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            user = request.POST.get('username')
            password = request.POST.get('password')
            account = authenticate(username=user, password=password)

            if account is not None:
                login(request, account)
                return redirect('tasks_list')
            else:
                messages.error(request, 'Incorrect Password os Username',extra_tags='login')

        context = {}
        return render(request, 'todo/login.html', context)

    else: 
        return redirect('tasks_list')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def tasks_list(request):
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(owner=request.user)
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_instance = form.save(commit=False)
            task_instance.owner = request.user
            task_instance.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/base.html', context)

@login_required(login_url='login')
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'todo/edit_task.html', {'form': form})

@login_required(login_url='login')
def delete_task (request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('/')
