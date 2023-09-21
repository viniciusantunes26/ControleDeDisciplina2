from rest_framework import serializers
from ..models.taskModel import TaskEntity

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskEntity
        fields = '__all__'