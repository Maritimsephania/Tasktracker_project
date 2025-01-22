from django.shortcuts import render
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

    tasks = Task.objects.all().values
    context['tasks'] = tasks
    context['title'] = 'tasks'
    return render(request, 'tasks.html',context)


def save(request):
    # Ensure access is via POST only
    # if request.method != "POST":
    #      return HttpResponseForbidden("Access denied.")
    
    context = {}
    form = TaskForm()
    context['title'] = 'save'
    if request.method == "POST":
        if 'save' in request.POST:
            form = TaskForm(request.POST)
            form.save()
             
    context['form']  =  form

    return render(request, 'save.html',context)
