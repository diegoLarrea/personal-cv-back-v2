from api.models import Persona
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombres', 'apellidos', 'documento', 'fecha_nacimiento', 'sexo', 'estado_civil'
        , 'pais_nacimiento', 'ciudad_residencia', 'email', 'cel_1', 'cel_2', 'telefono', 'foto_perfil'
        , 'familiares', 'ha_trabajado', 'user')