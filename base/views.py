from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import Task, SignUp
from .models import Todo
# Create your views here.

def home(request):
    form = Task
    context = {"form": form}

    if request.method == 'POST':
        form = Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/task')
    return render(request, 'base/index.html', context)


def task(request):
    todo = Todo.objects.all()
    context= {'todo': todo}
    return render(request, 'base/tasks.html', context)



def deletePage(request, pk):
    room = Todo.objects.get(id=pk)
    context = {"room": room}

    if request.method == 'POST':
        Todo.objects.get(id=pk).delete()
        return redirect('/task')
    return render(request, 'base/delete.html', context)

def create_user(request):
    creation = SignUp
    context = {"form": creation}
    return render(request, 'base/user.html', context)