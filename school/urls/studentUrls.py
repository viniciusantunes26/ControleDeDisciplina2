from django.contrib import admin
from django.urls import path

from school.views.studentView import StudentView
from school.views.studentList import StudentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentView.as_view(), name='student'),
    path('students/', StudentListView.as_view(), name='student-list'),
]