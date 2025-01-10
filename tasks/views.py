from django.shortcuts import render
#from django.template import loader
from .models import Task

# Create your views here.

def index(request):
    #mytasks = Task.objects.all().values
    #template = loader.get_template('tasks.html')
    context = {
        'tasks': Task
    }
    return render(request, 'index.html',context)

def tasks(request):
    context = {}
    return(request, 'tasks.html',context)