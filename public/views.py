from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from api.models import Task

def home_view(request):
    return render(request, 'public/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)  # Affiche les erreurs dans la console
    else:
        form = UserCreationForm()
    return render(request, 'public/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('tasks')
    else:
        form = AuthenticationForm()
    return render(request, 'public/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_list_view(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == "POST":
        task_title = request.POST.get('task')
        task = Task(user=request.user, title=task_title)
        task.save()
        return redirect('tasks')
    
    context = {
        'tasks': tasks,
    }
    return render(request, 'public/tasks.html', context)

@login_required
def mark_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.status = 'finished'
    task.save()
    return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('tasks')