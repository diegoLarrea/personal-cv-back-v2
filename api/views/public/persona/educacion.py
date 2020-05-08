from api.models import Educacion
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.serializers.persona.educacionSerializer import EducacionSerializer

class educacionList(APIView):

    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        educacion = Educacion.objects.filter(user=request.user)
        serializer = EducacionSerializer(educacion, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EducacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class educacionDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Educacion.objects.get(pk=pk)
        except Educacion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        educacion = self.get_object(pk)
        serializer = EducacionSerializer(educacion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        educacion = self.get_object(pk)
        serializer = EducacionSerializer(educacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        educacion = self.get_object(pk)
        educacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
