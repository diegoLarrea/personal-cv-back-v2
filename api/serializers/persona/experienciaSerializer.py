from api.models import Experiencia
from rest_framework import serializers

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = ('id','institucion' ,'rubro', 'puesto', 'trabajando', 'desde', 'hasta', 'tareas', 
        'superior_nombre', 'superior_puesto', 'superior_contacto', 'documento', 'ultima_modificacion', 'user')