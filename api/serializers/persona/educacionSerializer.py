from api.models import Educacion
from rest_framework import serializers

class EducacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educacion
        fields = ('id','institucion', 'titulo', 'nivel', 'pais', 'estudiando', 'desde'
        , 'hasta', 'ultima_modificacion', 'documento', 'user')