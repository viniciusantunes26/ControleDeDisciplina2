from rest_framework import serializers
from ..models.studentModel import StudentEntity

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntity
        fields = '__all__'
