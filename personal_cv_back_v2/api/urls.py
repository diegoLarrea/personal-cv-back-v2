from django.urls import include, path
from rest_framework import routers
from api.views.configViews.areaView import AreaList, AreaDetail
from api.views.configViews.dominioView import DominioList, DominioDetail
from api.views.configViews.nivelView import NivelList, NivelDetail
from api.views.configViews.localidadView import LocalidadList, LocalidadDetail
from api.views.ofertaLaboralView.ofertaLaboralView import OfertaList, OfertaDetail

urlpatterns = [
    path('area', AreaList.as_view()),
    path('area/<int:pk>', AreaDetail.as_view()),

    path('dominio', DominioList.as_view()),
    path('dominio/<int:pk>', DominioDetail.as_view()),

    path('nivel', NivelList.as_view()),
    path('nivel/<int:pk>', NivelDetail.as_view()),

    path('localidad', LocalidadList.as_view()),
    path('localidad/<int:pk>', LocalidadDetail.as_view()),

    path('oferta', OfertaList.as_view()),
    path('oferta/<int:pk>', OfertaDetail.as_view()),
]