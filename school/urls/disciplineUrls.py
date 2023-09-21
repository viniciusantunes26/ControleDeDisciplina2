from django.contrib import admin
from django.urls import path

from school.views.disciplineView import DisciplineView
from school.views.disciplineList import DisciplineListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', DisciplineView.as_view(), name='discipline'),
    path('students/', DisciplineListView.as_view(), name='discipline-list'),
]