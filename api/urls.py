from django.urls import include, path
from rest_framework import routers

# imports para public
from rest_framework_simplejwt import views as jwt_views
from api.views.public.register import register
from api.views.public.empleo import empleosList, obtenerFiltros
from api.views.public.captcha import captcha
from api.views.public.persona.persona import personaDetail
from api.views.public.persona.educacion import educacionList, educacionDetail
from api.views.public.persona.idioma import idiomaList, idiomaDetail
from api.views.public.persona.experiencia import experienciaList, experienciaDetail
from api.views.public.persona.referencia import referenciaList, referenciaDetail
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
    # URL CRUD educacion
    path('public/educacion', educacionList.as_view()),
    path('public/educacion/<int:pk>', educacionDetail.as_view()),
    # URL CRUD idioma
    path('public/idioma', idiomaList.as_view()),
    path('public/idioma/<int:pk>', idiomaDetail.as_view()),
    # URL CRUD experiencia
    path('public/experiencia', experienciaList.as_view()),
    path('public/experiencia/<int:pk>', experienciaDetail.as_view()),
    # URL CRUD referencia
    path('public/referencia', referenciaList.as_view()),
    path('public/referencia/<int:pk>', referenciaDetail.as_view()),
]