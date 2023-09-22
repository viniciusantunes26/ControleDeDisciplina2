from django.db import models

class StudentEntity(models.Model):

  """
    Modelo para representar uma entidade de estudante.

    Atributos:
        nome (CharField): O nome do estudante (comprimento máximo: 100).
        email (EmailField): O endereço de e-mail do estudante (único).
  """
      
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)

  def __str__(self) -> str:

    """
      Retorna uma representação de string legível do estudante.

      Retorna:
        str: Uma string no formato "Estudante [ID - Nome]".
    """

    return "Student [%i - %s]" % (self.id, self.name)