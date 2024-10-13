
from django.shortcuts import render
from todos.models import Task


def index(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


# def index(request):  # +
#     tasks = Task.objects.filter(is_completed=False)  # +
#     return render(request, 'index.html', {'tasks': tasks})  # +
