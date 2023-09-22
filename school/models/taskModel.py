from django.db import models
from .studentModel import StudentEntity
from .disciplineModel import DisciplineEntity

class TaskEntity(models.Model):

  """
    Modelo para representar uma tarefa.

    Atributos:
      title (CharField): O título da tarefa (máximo de 64 caracteres).
      description (TextField): A descrição da tarefa.
      date_delivery (DateField): A data de entrega da tarefa.
      concluded (BooleanField): Indica se a tarefa está concluída (padrão: True).
      student (ForeignKey): Uma referência ao StudentEntity relacionado, com exclusão em cascata.
      discipline (ManyToManyField): Uma referência ao DisciplineEntity relacionado.
  """

  title = models.CharField(max_length=64)
  description = models.TextField()
  date_delivery = models.DateField()
  concluded = models.BooleanField(default=True)
  student = models.ForeignKey(StudentEntity, on_delete=models.CASCADE)
  discipline = models.ManyToManyField(DisciplineEntity)

def __str__(self) -> str:
    
    """
      Retorna uma representação em string da tarefa.

      Retorna:
        str: Uma string contendo informações da tarefa.
    """

    return "Task [%i - %s - %d - %r]" % (self.id, self.title, self.concluded)