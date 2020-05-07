from rest_framework import generics
from api.models import Localidad
from api.serializers.ajustes.ajustes import LocalidadSerializer
from rest_framework.permissions import IsAuthenticated

class localidadList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer


class localidadDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer