from django import forms
from .models import project, task
#forms lo creas para crear formularios
#crear formulario para crear tareas
class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo', max_length=200)
    description = forms.CharField(label='Descripcion', widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del Proyecto', max_length=200)
    