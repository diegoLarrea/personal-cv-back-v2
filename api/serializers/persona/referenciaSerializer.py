from api.models import Referencia
from rest_framework import serializers

class ReferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referencia
        fields = ('id','nombre' ,'parentesco', 'contacto', 'ultima_modificacion', 'user')