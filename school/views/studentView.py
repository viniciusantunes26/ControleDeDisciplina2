from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from school.models.studentModel import StudentEntity
from school.serializers.studentSerializer import StudentSerializer

class StudentView(APIView):
    """
    List all categories, or create a new student.
    """
    def get(self, request, format=None):
        students = StudentEntity.objects.all()
        serializer = StudentSerializer  (students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)