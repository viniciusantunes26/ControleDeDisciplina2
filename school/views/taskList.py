from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from school.models.taskModel import TaskEntity
from school.serializers.taskSerializer import TaskSerializer

class TaskListView(APIView):
     
    def get(self,request,pk):
        try:
            task = TaskEntity.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        
        except TaskEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            task = TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            student = TaskEntity.objects.get(pk=pk)
        except TaskEntity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)