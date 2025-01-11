from django.shortcuts import render
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
    form = TaskForm
    tasks = Task.objects.all().values
    context['tasks'] = tasks
    context['title'] = 'tasks'
    context['form']  =  form
    return render(request, 'tasks.html',context)