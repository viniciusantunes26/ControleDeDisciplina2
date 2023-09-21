from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from school.models.disciplineModel import DisciplineEntity
from school.serializers.disciplineSerializer import DisciplineSerializer

class DisciplineView(APIView):
    
    def get(self, request):
        task = DisciplineEntity.objects.all()
        serializer = DisciplineSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)