from rest_framework import serializers
from django.contrib.auth.models import Permission

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["id", "name", "codename"] 
