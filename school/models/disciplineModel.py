# Importação necessária do Django para modelos
from django.db import models

class DisciplineEntity(models.Model):

  """
    Modelo para representar uma entidade de disciplina.

    Atributos:
        nome (CharField): O nome da disciplina (comprimento máximo: 64).
        descricao (TextField): Uma descrição da disciplina.
  """
   
  name = models.CharField(max_length=64)
  description = models.TextField()

  def __str__(self) -> str:

    """
      Retorna uma representação de string legível da disciplina.

      Retorna:
        str: Uma string no formato "Disciplina [ID - Nome]".
    """

    return "Discipline [%i - %s]" % (self.id, self.name)