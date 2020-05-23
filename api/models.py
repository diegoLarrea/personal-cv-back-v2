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

class Tag(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    user_tag = models.ManyToManyField(User, related_name="tags")

class Empleo(models.Model):
    oportunidad = models.CharField(max_length=200)
    descripcion = models.TextField()
    requisitos = models.TextField()
    tipo_choices = Choices("Interna", "Externa")
    tipo = models.CharField(choices=tipo_choices, default=tipo_choices.Interna, max_length=7)
    vigencia = models.DateField(null=False)
    codigo = models.CharField(max_length=20, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    dominio = models.ForeignKey(Dominio, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(null=True)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_add")
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_edit")

class Postulacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postulaciones')
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE, related_name='postulantes')
    fecha_postulacion = models.DateTimeField(auto_now_add=True)

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField(null=True)
    sexo_choices = Choices("F", "M")
    sexo = models.CharField(choices=sexo_choices, max_length=1, null=True)
    estado_civil = models.CharField(max_length=20, null=True)
    pais_nacimiento = models.CharField(max_length=100, null=True)
    ciudad_residencia = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    cel_1 = models.CharField(max_length=50, null=True)
    cel_2 = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=50, null=True)
    foto_perfil = models.TextField(null=True)
    familiares = models.TextField(null=True)
    ha_trabajado = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    estados_choices = Choices("Ingresado", "Visto", "Seleccionado", "Contratado")
    estado = models.CharField(choices=estados_choices, max_length=20, default="Ingresado")

class Educacion(models.Model):
    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    nivel = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)
    estudiando = models.BooleanField(default=False)
    desde = models.CharField(max_length=20)
    hasta = models.CharField(max_length=20, null=True, blank=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    documento = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Idioma(models.Model):
    idioma = models.CharField(max_length=50)
    niveles = Choices("B", "I", "A", "N")
    habla = models.CharField(choices=niveles, max_length=1, default='B')
    lee = models.CharField(choices=niveles, max_length=1, default='B')
    escribe = models.CharField(choices=niveles, max_length=1, default='B')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Experiencia(models.Model):
    institucion = models.CharField(max_length=200)
    rubro = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    trabajando = models.BooleanField(default=False)
    desde = models.CharField(max_length=20)
    hasta = models.CharField(max_length=20, null=True, blank=True)
    tareas = models.TextField()
    superior_nombre = models.CharField(max_length=200)
    superior_puesto = models.CharField(max_length=200)
    superior_contacto = models.CharField(max_length=200)
    documento = models.TextField()
    ultima_modificacion = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Referencia(models.Model):
    nombre = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)