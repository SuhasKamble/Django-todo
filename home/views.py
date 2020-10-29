from django.shortcuts import render, HttpResponse
from home.models import Task
# Create your views here.


def home(request):
    context = {"success": False}
    if request.method == "POST":
        # handle the form
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        ins = Task(title=title, desc=desc)
        ins.save()
        context = {"success": True}
    return render(request, 'index.html', context)


def tasks(request):
    allTasks = Task.objects.all()
    context = {"tasks": allTasks}
    return render(request, 'tasks.html', context)
