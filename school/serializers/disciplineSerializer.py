from rest_framework import serializers
from ..models.disciplineModel import DisciplineEntity

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineEntity
        fields = '__all__'
