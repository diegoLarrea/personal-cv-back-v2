from api.models import Idioma
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.serializers.persona.idiomaSerializer import IdiomaSerializer

class idiomaList(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        idiomas = Idioma.objects.filter(user=request.user)
        serializer = IdiomaSerializer(idiomas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IdiomaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class idiomaDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Idioma.objects.get(pk=pk)
        except Idioma.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idioma = self.get_object(pk)
        serializer = IdiomaSerializer(idioma)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        idioma = self.get_object(pk)
        serializer = IdiomaSerializer(idioma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        idioma = self.get_object(pk)
        idioma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
