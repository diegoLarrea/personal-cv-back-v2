from rest_framework import generics
from api.models import Dominio
from api.serializers.ajustes.ajustes import DominioSerializer
from rest_framework.permissions import IsAuthenticated

class dominioList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer


class dominioDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer