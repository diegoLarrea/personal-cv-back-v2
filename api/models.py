from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices

class Area(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        permissions = ( 
            ( "api_listar_areas", "Listar areas" ),
            ( "api_crear_area", "Agregar area" ),
            ( "api_editar_area", "Editar area" ),
            ( "api_eliminar_area", "Eliminar area" ),
        )

class Dominio(models.Model):
    nombre = models.CharField(max_length=100)
    
    class Meta:
        permissions = ( 
            ( "api_listar_dominios", "Listar dominios" ),
            ( "api_crear_dominio", "Agregar dominio" ),
            ( "api_editar_dominio", "Editar dominio" ),
            ( "api_eliminar_dominio", "Eliminar dominio" ),
        )

class Nivel(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        permissions = ( 
            ( "api_listar_niveles", "Listar niveles" ),
            ( "api_crear_nivel", "Agregar nivel" ),
            ( "api_editar_nivel", "Editar nivel" ),
            ( "api_eliminar_nivel", "Eliminar nivel" ),
        )

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    class Meta:
        permissions = ( 
            ( "api_listar_localidades", "Listar localidades" ),
            ( "api_crear_localidad", "Agregar localidad" ),
            ( "api_editar_localidad", "Editar localidad" ),
            ( "api_eliminar_localidad", "Eliminar localidad" ),
        )

class Empleo(models.Model):
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

    class Meta:
        permissions = ( 
            ( "api_listar_empleos", "Listar empleos" ),
            ( "api_crear_empleo", "Agregar empleo" ),
            ( "api_editar_empleo", "Editar empleo" ),
            ( "api_eliminar_empleo", "Eliminar empleo" ),
        )

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

    class Meta:
        permissions = ( 
            ( "api_editar_persona", "Editar datos personales" ),
        )

class Postulacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    fecha_postulacion = models.DateField()

    class Meta:
        permissions = ( 
            ( "api_listar_postulaciones", "Listar postulaciones" ),
            ( "api_crear_postulacion", "Agregar postulacion" ),
            ( "api_editar_postulacion", "Editar postulacion" ),
            ( "api_eliminar_postulacion", "Eliminar postulacion" ),
        )