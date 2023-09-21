from django.contrib import admin
from django.urls import path

from school.views.taskView import TaskView
from school.views.taskList import TaskListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', TaskView.as_view(), name='task'),
    path('students/', TaskListView.as_view(), name='task-list'),
] 