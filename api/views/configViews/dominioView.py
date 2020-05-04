from rest_framework import generics
from api.models import Dominio
from api.serializers.configSerializer.configSerializer import DominioSerializer


class DominioList(generics.ListCreateAPIView):
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer


class DominioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer