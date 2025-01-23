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
        

            
    return render(request, 'tasks.html',context)


# def save(request):
#     # Ensure access is via POST only
#     # if request.method != "POST":
#     #      return HttpResponseForbidden("Access denied.")
    
#     context = {}
#     form = TaskForm()#request.POST or None)
#     context['title'] = 'save'
#     if request.method == "POST":
#         if 'save' in request.POST:
#             #if form.is_valid():
#             form = TaskForm(request.POST)
#             form.save()
#             return redirect('tasks')
#     else:
#            return HttpResponseForbidden("Access denied.") 
#     context['form']  =  form

#     return render(request, 'save.html',context)


def save(request):
    context = {'title': 'save'}
    form = TaskForm(request.POST or None)  # Initialize the form with POST data if available

    if request.method == "POST":
        if 'save' in request.POST:
            form = TaskForm(request.POST)
            form.save() 
            return redirect('tasks')
        elif 'edit' in request.POST:
            primary_key = request.POST.get('edit')
            task = Task.objects.get(id = primary_key)
            form = TaskForm(instance= task)
    else:
        return HttpResponseForbidden("Access denied.") 


    context['form'] = form 
    return render(request, 'save.html', context)
