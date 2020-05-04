from rest_framework import generics
from api.models import Area
from api.serializers.configSerializer.configSerializer import AreaSerializer
from rest_framework.permissions import IsAuthenticated


class AreaList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Area.objects.all()
    serializer_class = AreaSerializer