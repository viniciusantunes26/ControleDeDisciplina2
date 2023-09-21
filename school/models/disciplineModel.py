from django.db import models

class DisciplineEntity(models.Model):
  name = models.CharField(max_length=64)
  description = models.TextField()

  def __str__(self) -> str:
    return "Discipline [%i - %s]" % (self.id, self.name)