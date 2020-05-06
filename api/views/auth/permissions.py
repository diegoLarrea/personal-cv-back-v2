from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User, Group, Permission

from api.serializers.permisos.permisos import PermisoSerializer
import json

@api_view(['GET'])
@permission_classes([AllowAny])
def get_permissions(request):
    groups = request.user.groups.all().values_list('id', flat=True)
    permisos =  Permission.objects.filter(group__id__in=groups)
    serializer = PermisoSerializer(permisos, many=True)
    return Response(serializer.data)