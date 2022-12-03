from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import TaskForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from datetime import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_todo': data_todolist,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def add_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user=User.objects.get(username=request.user.username)
            data.save()
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'addtask.html', context)

def change_status(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST["id"])
        task.is_finished = not(task.is_finished)
        task.save()
    return redirect('todolist:show_todolist')

def delete_task(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST["id"])
        task.delete()
    return redirect('todolist:show_todolist')

#Tugas 6: AJAX 

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    return render(request, "todolist_ajax.html")

@login_required(login_url='/todolist/login/')
def add_task_ajax(request):
    if request.method == 'POST':
        titleBaru = request.POST.get('title')
        descBaru = request.POST.get('description')
        new_task = Task(
            user = request.user,
            date = datetime.now(),
            title = titleBaru,
            description = descBaru,
            is_finished = False,
        )
        new_task.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()