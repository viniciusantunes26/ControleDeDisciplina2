# Importações necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos e serializadores
from school.models.taskModel import TaskEntity
from school.serializers.taskSerializer import TaskSerializer

class TaskView(APIView):
    
    # Método GET para listar todas as tarefas
    def get(self, request):
        task = TaskEntity.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    # Método POST para criar uma nova tarefa
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)