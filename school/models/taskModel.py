from django.db import models
from .studentModel import StudentEntity
from .disciplineModel import DisciplineEntity

class TaskEntity(models.Model):
  title = models.CharField(max_length=64)
  description = models.TextField()
  date_delivery = models.DateField()
  concluded = models.BooleanField(default=True)
  student = models.ForeignKey(StudentEntity, on_delete=models.CASCADE)
  discipline = models.ManyToManyField(DisciplineEntity)

def __str__(self) -> str:
    return "Task [%i - %s - %d - %r]" % (self.id, self.title, self.concluded)