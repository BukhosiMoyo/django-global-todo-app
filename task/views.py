from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def HomeListView(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request, "task/home.html", context)


def TaskCreateView(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    context = {"form": form}
    return render(request, "task/create.html", context)

def TaskUpdateView(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {"form":form, "task":tasks}
    return render(request, "task/update.html", context)

def TaskDeleteView(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        
        task.delete()

        return redirect("/")
    context = {"item":task}
    return render(request, "task/delete.html", context)






