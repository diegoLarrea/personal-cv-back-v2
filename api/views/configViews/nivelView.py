from rest_framework import generics
from api.models import Nivel
from api.serializers.configSerializer.configSerializer import NivelSerializer


class NivelList(generics.ListCreateAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer


class NivelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer