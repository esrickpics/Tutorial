from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'), 
    path('about/', views.about, name ='about'), #name es un alias para la url
    path('hello/<str:username>', views.hello),
    path('hola/<int:id>', views.hola), 
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name = 'create_project'),
]
 