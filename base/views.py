from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import Task, SignUp, NewUserForm
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    form = Task
    current_user = request.user.id

    if request.method == 'POST':
        form = Task(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user =request.user
            task.save()
            return redirect('/task')
    context = {"form": form}
    return render(request, 'base/index.html', context)

@login_required(login_url='/login')
def task(request):
    #todo = Todo.objects.all()
    current_user = request.user.id

    todo = Todo.objects.filter(user=current_user)

    context= {'todo': todo}
    return render(request, 'base/tasks.html', context)


@login_required(login_url='/login')
def deletePage(request, pk):
    room = Todo.objects.get(id=pk)
    context = {"room": room}

    if request.method == 'POST':
        Todo.objects.get(id=pk).delete()
        return redirect('/task')
    return render(request, 'base/delete.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(username=username,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

        

    return render(request, 'base/user.html')


def signup(request):
    form = NewUserForm()
    context = {"form": form}
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    return render(request, 'base/sign.html', context)


@login_required(login_url='/login')
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('/login')
    return render(request, 'base/logout.html')