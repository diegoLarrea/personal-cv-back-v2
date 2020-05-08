from api.models import Idioma
from rest_framework import serializers

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ('id','idioma' ,'habla', 'lee', 'escribe', 'user')