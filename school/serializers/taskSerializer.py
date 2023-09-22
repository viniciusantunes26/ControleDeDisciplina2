# Importações necessárias do Django REST framework e do modelo TaskEntity
from rest_framework import serializers
from ..models.taskModel import TaskEntity

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskEntity  # Define o modelo associado ao serializador
        fields = '__all__'  # Define que todos os campos do modelo que devem ser incluídos na serialização