from api.models import Postulacion
from api.serializers.empleo.postulacionSerializer import PostulacionSerializer, PostulacionDepthSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class postulacionList(APIView):
    
    def get(self, request, format=None):
        postulaciones = Postulacion.objects.filter(user=request.user)
        serializer = PostulacionDepthSerializer(postulaciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostulacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class postulacionDetail(APIView):
    def get_object(self, pk):
        try:
            return Postulacion.objects.get(pk=pk)
        except Postulacion.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        postulacion = self.get_object(pk)
        postulacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)