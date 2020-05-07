from django.urls import include, path
from rest_framework import routers

# imports para public
from rest_framework_simplejwt import views as jwt_views
from api.views.public.register import register
from api.views.public.empleo import empleosList, obtenerFiltros
from api.views.public.captcha import captcha
from api.views.public.persona import personaDetail
from api.views.public.usuario import getUsuario

urlpatterns = [

    ## URL publicas ##

    # URL para login
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    # URL para registro de usuarios
    path('registrarse', register),
    # URL para obtener captcha
    path('captcha', captcha),
    # URL para obtener permisos de un usuario
    path('obtener-usuario-logueado', getUsuario),
    # URL para obtener empleos
    path('public/empleos', empleosList),
    # URL para obtener empleos
    path('public/empleos/obtener-filtros', obtenerFiltros),
    # URL para obtener y actualizar persona
    path('public/persona/<int:pk>', personaDetail.as_view()),
]