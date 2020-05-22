from api.models import Dominio
from api.serializers.ajustes.ajustesSerializers import DominioSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class dominioList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        dominios = Dominio.objects.all()
        serializer = DominioSerializer(dominios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DominioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class dominioDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Dominio.objects.get(pk=pk)
        except Dominio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dominio = self.get_object(pk)
        serializer = DominioSerializer(dominio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dominio = self.get_object(pk)
        serializer = DominioSerializer(dominio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dominio = self.get_object(pk)
        dominio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
