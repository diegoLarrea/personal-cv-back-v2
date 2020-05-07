from rest_framework import generics
from api.models import Nivel
from api.serializers.ajustes.ajustes import NivelSerializer
from rest_framework.permissions import IsAuthenticated

class nivelList(generics.ListCreateAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer


class nivelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer