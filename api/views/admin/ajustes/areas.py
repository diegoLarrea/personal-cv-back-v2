from rest_framework import generics
from api.models import Area
from api.serializers.ajustes.ajustes import AreaSerializer
from rest_framework.permissions import IsAuthenticated


class areaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class areaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer