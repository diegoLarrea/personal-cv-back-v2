from rest_framework import serializers
from api.models import Empleo

class EmpleoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleo
        # depth = 1
        fields = ["id", "oportunidad", "descripcion", "requisitos", "tipo", "vigencia", "localidad", "area", 
        "dominio", "nivel", "fecha_creacion", "fecha_modificacion", "usuario_creacion", "usuario_modificacion"] 