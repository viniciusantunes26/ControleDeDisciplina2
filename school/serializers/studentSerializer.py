# Importações necessárias do Django REST framework e do modelo StudentEntity
from rest_framework import serializers
from ..models.studentModel import StudentEntity

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntity  # Define o modelo associado ao serializador
        fields = '__all__'     # Define que todos os campos do modelo que devem ser incluídos na serialização
