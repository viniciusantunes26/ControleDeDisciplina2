# Importações necessárias do Django e do Django REST framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importando os modelos e serializadores
from school.models.studentModel import StudentEntity
from school.serializers.studentSerializer import StudentSerializer

class StudentListView(APIView):

    # Método auxiliar para obter um objeto StudentEntity por sua chave primária (pk)
    def get_object(self, pk):
        try:
            return StudentEntity.objects.get(pk=pk)
        except StudentEntity.DoesNotExist:
            raise Http404
        
    # Método GET para listar informações de um estudante por pk
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # Método PUT para atualizar informações de um estudante por pk
    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Método DELETE para excluir um estudante por pk
    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)