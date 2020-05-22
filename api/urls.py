from django.urls import include, path
from rest_framework import routers

# imports para public
from rest_framework_simplejwt import views as jwt_views
from api.views.public.register import register
from api.views.public.empleo import empleosList, obtenerFiltros, getEmpleoById
from api.views.public.captcha import captcha
from api.views.public.persona.persona import personaDetail, personaDataAll
from api.views.public.persona.educacion import educacionList, educacionDetail
from api.views.public.persona.idioma import idiomaList, idiomaDetail
from api.views.public.persona.experiencia import experienciaList, experienciaDetail
from api.views.public.persona.referencia import referenciaList, referenciaDetail
from api.views.public.postulacion import postulacionList, postulacionDetail
from api.views.public.usuario import getUsuario

# imports para admin
from api.views.admin.user.user import userList
from api.views.admin.ajustes.areas import areaList,areaDetail
from api.views.admin.ajustes.niveles import nivelList,nivelDetail
from api.views.admin.ajustes.dominios import dominioList,dominioDetail
from api.views.admin.ajustes.localidades import localidadList,localidadDetail
from api.views.admin.ajustes.tags import tagList,tagDetail

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
    path('public/empleos/<int:pk>', getEmpleoById),
    # URL para obtener empleos
    path('public/empleos/obtener-filtros', obtenerFiltros),
    # URL para obtener y actualizar persona
    path('public/persona/<int:pk>', personaDetail.as_view()),
    # URL para obtener todos los datos de la persona
    path('public/persona/all', personaDataAll.as_view()),
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
    # URL CRUD postulaciones
    path('public/postulacion', postulacionList.as_view()),
    path('public/postulacion/<int:pk>', postulacionDetail.as_view()),

    ## URL admin ##
    path('admin/usuarios', userList.as_view()),
    # URL CRUD area
    path('admin/area', areaList.as_view()),
    path('admin/area/<int:pk>', areaDetail.as_view()),
    # URL CRUD nivel
    path('admin/nivel', nivelList.as_view()),
    path('admin/nivel/<int:pk>', nivelDetail.as_view()),
    # URL CRUD dominio
    path('admin/dominio', dominioList.as_view()),
    path('admin/dominio/<int:pk>', dominioDetail.as_view()),
    # URL CRUD localidades
    path('admin/localidad', localidadList.as_view()),
    path('admin/localidad/<int:pk>', localidadDetail.as_view()),
    # URL CRUD tags
    path('admin/tag', tagList.as_view()),
    path('admin/tag/<int:pk>', tagDetail.as_view()),
]