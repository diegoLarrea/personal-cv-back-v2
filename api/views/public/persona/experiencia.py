from api.models import Experiencia
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.serializers.persona.experienciaSerializer import ExperienciaSerializer

class experienciaList(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        experiencia = Experiencia.objects.filter(user=request.user)
        serializer = ExperienciaSerializer(experiencia, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExperienciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class experienciaDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Experiencia.objects.get(pk=pk)
        except Experiencia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        experiencia = self.get_object(pk)
        serializer = ExperienciaSerializer(experiencia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        experiencia = self.get_object(pk)
        serializer = ExperienciaSerializer(experiencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        experiencia = self.get_object(pk)
        experiencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
