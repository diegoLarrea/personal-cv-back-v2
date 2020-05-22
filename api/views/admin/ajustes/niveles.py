from api.models import Nivel
from api.serializers.ajustes.ajustesSerializers import NivelSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class nivelList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        niveles = Nivel.objects.all()
        serializer = NivelSerializer(niveles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NivelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class nivelDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Nivel.objects.get(pk=pk)
        except Nivel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nivel = self.get_object(pk)
        serializer = NivelSerializer(nivel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        nivel = self.get_object(pk)
        serializer = NivelSerializer(nivel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nivel = self.get_object(pk)
        nivel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
