from api.models import Persona 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from rest_framework.permissions import IsAuthenticated
from api.helpers.check import check_permissions
from api.serializers.persona.persona import PersonaSerializer
from datetime import datetime

class personaList(APIView):
    """
    Lista todas las ofertas, o crea una nueva oferta.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        if not check_permissions(request.user, 'api.api_listar_curriculums'):
            return Response(status=status.HTTP_403_FORBIDDEN)

        personas = Persona.objects.all()
        
        serializer = PersonaSerializer(personas, many=True)

        return Response(serializer.data)
        

class personaDetail(APIView):
    """
    Retrieve, update or delete a oferta instance.
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Persona.objects.get(user=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
