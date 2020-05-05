from django.urls import include, path
from rest_framework import routers
from api.views.auth.register import register
from rest_framework_simplejwt import views as jwt_views
from api.views.ajustes.areas import areaList, areaDetail
from api.views.ajustes.dominios import dominioList, dominioDetail
from api.views.ajustes.niveles import nivelList, nivelDetail
from api.views.ajustes.localidades import localidadList, localidadDetail
from api.views.ofertaLaboral.ofertaLaboral import ofertaList, ofertaDetail


urlpatterns = [
    # URL para registro de usuarios
    path('registrarse', register),

    # URL para login
    path('login', jwt_views.TokenObtainPairView.as_view(),name='login'),
        # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),

    # URL para ajustes 
    path('area', areaList.as_view()),
    path('area/<int:pk>', areaDetail.as_view()),
    path('dominio', dominioList.as_view()),
    path('dominio/<int:pk>', dominioDetail.as_view()),
    path('nivel', nivelList.as_view()),
    path('nivel/<int:pk>', nivelDetail.as_view()),
    path('localidad', localidadList.as_view()),
    path('localidad/<int:pk>', localidadDetail.as_view()),

    # URL para ofertas
    path('oferta', ofertaList.as_view()),
    path('oferta/<int:pk>', ofertaDetail.as_view()),

]