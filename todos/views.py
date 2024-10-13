from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
# Create your views here.


def addTask(request):
    # return render(request, 'add_task.html')
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('index')