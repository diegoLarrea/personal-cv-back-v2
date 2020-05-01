from rest_framework import generics
from api.models import Area
from api.serializers.configSerializer.configSerializer import AreaSerializer


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer