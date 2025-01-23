from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
#from django.template import loader
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    #template = loader.get_template('tasks.html')
    context = {}
    context['title'] = 'home'

    return render(request, 'index.html',context)

def tasks(request):
    context = {}
    form = TaskForm()

    tasks = Task.objects.all().values
    context['tasks'] = tasks
    context['title'] = 'tasks'
    if request.method == 'POST':
        if 'delete' in request.POST:
            primary_key = request.POST.get('delete')
            task = Task.objects.get(id = primary_key)
            task.delete()
            return redirect('tasks')
        elif 'edit' in request.POST:
             primary_key = request.POST.get('edit')
             task = Task.objects.get(id = primary_key)
             form = TaskForm(instance= task)
            
             return render(request, 'save.html', {'form': form, 'task_id': primary_key})
        

            
    return render(request, 'tasks.html',context)


def save(request):
    context = {}

    context['title'] = 'save'
    form = TaskForm()  # Initialize the form with POST data if available

    if request.method == "POST":
        if 'save' in request.POST:
            primary_key =request.POST.get('save')
            if not primary_key:
                form = TaskForm(request.POST)
            else:
                task = Task.objects.get(id=primary_key)
                form = TaskForm(request.POST,instance=task)
            form.save() 
            return redirect('tasks')
        # elif 'edit' in request.POST:
        #     primary_key = request.POST.get('edit')
        #     task = Task.objects.get(id = primary_key)
        #     form = TaskForm(instance= task)
    else:
        return HttpResponseForbidden("Access denied.") 


    context['form'] = form 
    return render(request, 'save.html', context)
