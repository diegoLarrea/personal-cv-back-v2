from api.models import Persona, Educacion, Idioma, Experiencia, Referencia
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.serializers.persona.personaSerializer import PersonaSerializer
from api.serializers.persona.educacionSerializer import EducacionSerializer
from api.serializers.persona.experienciaSerializer import ExperienciaSerializer
from api.serializers.persona.idiomaSerializer import IdiomaSerializer
from api.serializers.persona.referenciaSerializer import ReferenciaSerializer
        
class personaDetail(APIView):

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

class personaDataAll(APIView):
    def get(self, request):
        persona = Persona.objects.get(user=request.user)
        educacion = Educacion.objects.filter(user=request.user)
        idiomas = Idioma.objects.filter(user=request.user)
        experiencias = Experiencia.objects.filter(user=request.user)
        referencias = Referencia.objects.filter(user=request.user)

        response = {
            "persona": PersonaSerializer(persona).data,
            "educacion": EducacionSerializer(educacion, many=True).data,
            "idiomas": IdiomaSerializer(idiomas, many=True).data,
            "experiencias": ExperienciaSerializer(experiencias, many=True).data,
            "referencias": ReferenciaSerializer(referencias, many=True).data
        }

        return Response(response)
