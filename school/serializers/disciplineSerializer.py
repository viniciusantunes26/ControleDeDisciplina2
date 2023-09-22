# Importações necessárias do Django REST framework e do modelo DisciplineEntity
from rest_framework import serializers
from ..models.disciplineModel import DisciplineEntity

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineEntity # Define o modelo associado ao serializador
        fields = '__all__'       # Define que todos os campos do modelo que devem ser incluídos na serialização
