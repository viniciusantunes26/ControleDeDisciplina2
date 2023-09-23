"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importações necessárias do Django
from django.contrib import admin
from django.urls import path

# Importações das visualizações personalizadas do aplicativo
from school.views.studentView import StudentView
from school.views.studentList import StudentListView
from school.views.disciplineView import DisciplineView
from school.views.disciplineList import DisciplineListView
from school.views.taskView import TaskView
from school.views.taskList import TaskListView

# Lista de urlpatterns que define as rotas da API
urlpatterns = [
    # Rota para a área administrativa do Django
    path('api/admin/', admin.site.urls),
    # Rotas para as visualizações relacionadas a estudantes (students)
    path('api/students/', StudentView.as_view(), name='student-list'),
    path('api/students/<int:pk>/', StudentListView.as_view(), name='student-detail'),
    # Rotas para as visualizações relacionadas a disciplinas (disciplines)
    path('api/disciplines/', DisciplineView.as_view(), name='discipline-list'),
    path('api/disciplines/<int:pk>/', DisciplineListView.as_view(), name='discipline-detail'),
    # Rotas para as visualizações relacionadas a tarefas (tasks)
    path('api/tasks/', TaskView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskListView.as_view(), name='task-detail'),
]
