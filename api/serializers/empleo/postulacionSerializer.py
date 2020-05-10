from api.models import Postulacion
from rest_framework import serializers

class PostulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = ('id','fecha_postulacion', 'user', 'empleo')

class PostulacionDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        depth = 1
        fields = ('id','fecha_postulacion', 'empleo')