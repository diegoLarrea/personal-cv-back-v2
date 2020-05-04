from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices

class Area(models.Model):
    nombre = models.CharField(max_length=100)

class Dominio(models.Model):
    nombre = models.CharField(max_length=100)

class Nivel(models.Model):
    nombre = models.CharField(max_length=100)

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

class OfertaLaboral(models.Model):
    oportunidad = models.CharField(max_length=200)
    descripcion = models.TextField()
    requisitos = models.TextField()
    tipo_choices = Choices("Interna", "Externa")
    tipo = models.CharField(choices=tipo_choices, default=tipo_choices.Interna, max_length=7)
    vigencia = models.DateTimeField(null=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    dominio = models.ForeignKey(Dominio, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(null=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_add")
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_edit")
