from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def deleteTask(request, id):
    delete_task = Task.objects.get(id=id)

    if request.method == 'POST':
        delete_task.delete()
        return redirect('/')

    context = {'delete_task': delete_task}
    return render(request, 'tasks/delete.html', context)

def editTask(request, id):
    edit_task = Task.objects.get(id=id)

    context = {'edit_task': edit_task}
    return render(request, 'tasks/edit.html', context)

def updateTask(request, id):
    uptdate_task = Task.objects.get(id=id)
    uptdate_task.title = request.POST['title']
    uptdate_task.complete = bool(request.POST.get('complete'))
    uptdate_task.save()
    return redirect('/', uptdate_task.id)