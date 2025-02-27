from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import project, task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def index(request):
    title = 'Bienvenido a la web con Django'
    return render (request, 'index.html', {
        'title': title #pasar variable a la vista
    })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" %username)

def hola (request, id):
    print(type(id))
    result = id + 10
    return HttpResponse("<h1>Hola %s</h1>" %result)

def about (request):
    return HttpResponse("About me")

def projects (request):
    projects = project.objects.all()
    return render(request, 'project/projects.html', {
        'projects': projects
    })

def tasks (request):
    tarea = task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tarea
    })

def create_task(request):
    if request.method == 'GET': #Si el metodo es GET, Get es para optener datos de la url
       return render(request, 'tasks/create_task.html', {
           'form': CreateNewTask()
       })
    else:
        task.objects.create(title=request.POST['title'],
        description=request.POST['description'], project_id=1)
        return redirect('/tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        proyecto = project.objects.create(name=request.POST['name'])
        return redirect('/projects')
        

    