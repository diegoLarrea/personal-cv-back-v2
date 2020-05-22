from rest_framework import serializers
from api.models import Nivel, Localidad, Area, Dominio, Tag

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = ["id", "nombre"] 

class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = ["id", "nombre", "direccion"] 

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "nombre"] 

class DominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dominio
        fields = ["id", "nombre"] 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "nombre", "color"] 
