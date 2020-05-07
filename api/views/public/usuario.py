from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User, Group, Permission
import json
from api.serializers.permiso.permisoSerializer import PermisoSerializer
from api.serializers.user.userSerializer import UserSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def getUsuario(request):
    groups = request.user.groups.all().values_list('id', flat=True)
    permisos =  Permission.objects.filter(group__id__in=groups)
    serializer_permisos = PermisoSerializer(permisos, many=True)
    serializer_user = UserSerializer(request.user)

    response={
        "usuario": serializer_user.data,
        "permisos": serializer_permisos.data
    }
    return Response(response)