from rest_framework import serializers
from api.models import OfertaLaboral

class OfertaLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaLaboral
        fields = ["id", "oportunidad", "descripcion", "requisitos", "tipo", "vigencia", "localidad", "area", 
        "dominio", "nivel", "fecha_creacion", "fecha_modificacion", "usuario_creacion", "usuario_modificacion"] 