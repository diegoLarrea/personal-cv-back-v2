from rest_framework import generics
from api.models import Localidad
from api.serializers.configSerializer.configSerializer import LocalidadSerializer


class LocalidadList(generics.ListCreateAPIView):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer


class LocalidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer