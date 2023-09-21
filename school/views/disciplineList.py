from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from school.models.disciplineModel import DisciplineEntity
from school.serializers.disciplineSerializer import DisciplineSerializer

class DisciplineListView(APIView):
     
    def get(self,request,pk):
        try:
            task = DisciplineEntity.objects.get(pk=pk)
            serializer = DisciplineSerializer(task)
            return Response(serializer.data)
        
        except DisciplineEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            task = DisciplineEntity.objects.get(pk=pk)
        except DisciplineEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DisciplineSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            student = DisciplineEntity.objects.get(pk=pk)
        except DisciplineEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)