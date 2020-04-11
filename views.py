from django.shortcuts import render,redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task is Inserted.')
        return redirect('index')
    else:
        task = TaskList.objects.all()
        return render(request,'todolist_app/index.html',{'tasklist':task})

def task_delete(request,task_id):
    task = TaskList.objects.get(pk=task_id)        
    task.delete()
    messages.success(request, 'Task is deleted successfully.')
    return redirect('index')

def edit_task(request,task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id) 
        form = TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, 'Task is Edited.')
        return redirect('index')
    else:
        s_task = TaskList.objects.get(pk=task_id)
        return render(request,'todolist_app/edit.html',{'s_task':s_task})

def mark_as_completed(request,task_id):
    task = TaskList.objects.get(pk=task_id)        
    task.done = True
    task.save()
    return redirect('index')   

def mark_as_pending(request,task_id):
    task = TaskList.objects.get(pk=task_id)        
    task.done = False
    task.save()
    return redirect('index')        
