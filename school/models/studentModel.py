from django.db import models

class StudentEntity(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)

  def __str__(self) -> str:
    return "Student [%i - %s]" % (self.id, self.name)