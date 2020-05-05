from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from api.serializers.user.user import UserSerializer
from api.models import Persona
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def register(self, request, format=None):
        
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    user, created = User.objects.get_or_create(username=body_data.get('email'),   
                                                    email=body_data.get('email'))

    check_persona = Persona.objects.filter(documento=body_data.get("documento")).count()
    
    if not created:
        return Response({"mensaje":"La cuenta ya existe"}, status=status.HTTP_400_BAD_REQUEST) 

    if check_persona > 0:
        return Response({"mensaje":"El nro. de documento ya fue registrado"}, status=status.HTTP_400_BAD_REQUEST)    

    user.first_name = body_data.get("nombres")
    user.last_name = body_data.get("apellidos")    
    user.set_password(body_data.get('password'))
    user.save()
    
    persona = Persona.objects.create(nombres=body_data.get('nombres'),
                                    apellidos=body_data.get('apellidos'),
                                    documento=body_data.get('documento'),
                                    user=user)
    persona.save()
    serializer = UserSerializer(user)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
