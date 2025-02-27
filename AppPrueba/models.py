from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() #textos largos
    done = models.BooleanField(default=False)
    project = models.ForeignKey(project, on_delete=models.CASCADE) #el onl_delete es para que si se borra un proyecto se borren las tareas asociadas
    #relacion uno a muchos con la tabla project

    def __str__(self):
        return self.title + ' - ' + self.project.name #mostrar titulo de la tarea y nombre del proyecto en /admin

   
    #para crear datos dentro usamos django shell

    #python manage.py shell
    #from AppPrueba.models import project, task
    #p = project(name='Proyecto 1', description='Descripcion del proyecto 1')
    #p.save()
    #p = project.objects.get(id=1)
    #p.task_set.create(title='Tarea 1', description='Descripcion de la tarea 1') crear tarea relacionada a proyecto
    #project.objects.filter(name__startswith='Proyecto') #buscar proyectos que empiecen con Proyecto
    #project.objects.filter(name__contains='Proyecto') #buscar proyectos que contengan Proyecto
    #project.objects.filter(name__endswith='Proyecto') #buscar proyectos que terminen con Proyecto
    
