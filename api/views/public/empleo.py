from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator
import json

from api.models import Empleo, Localidad, Area, Postulacion
from api.serializers.empleo.empleoSerializer import EmpleoSerializer
from api.serializers.ajustes.ajustesSerializers import LocalidadSerializer, AreaSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def empleosList(request):
    
    ofertas = Empleo.objects.all()

    # Query Params
    page = request.GET.get('page', 1)
    itemsPP = request.GET.get('cantidad', 10)
    orderBy = request.GET.get('orderBy', "fecha_creacion")
    orderDir = request.GET.get('orderDir', "-")
    oportunidad = request.GET.get("oportunidad", None)
    filters = request.GET.get('filters', None)

    if filters is not None:
        filters = json.loads(filters)
        areas_json = filters.get("areas", None)
        localidades_json = filters.get("localidades", None)
    
        areas_ids = []
        localidades_ids = []

        if areas_json is not None:
            for area in areas_json:
                areas_ids.append(area["id"])
            ofertas = ofertas.filter(area__in=areas_ids)

        if localidades_json is not None:
            for localidad in localidades_json:
                localidades_ids.append(localidad["id"])
            ofertas = ofertas.filter(localidad__in=localidades_ids)        

    if oportunidad is not None:
        ofertas = ofertas.filter(oportunidad__contains=oportunidad)

    ofertas = ofertas.order_by("%s%s" % (orderDir, orderBy))

    paginator = Paginator(ofertas, itemsPP)
    empleos = paginator.page(page)

    serializer = EmpleoSerializer(empleos, many=True)
    
    response = {
        "items": serializer.data,
        "total": ofertas.count()
    }
    return Response(response)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtenerFiltros(request):
    areas = Area.objects.all()
    localidades = Localidad.objects.all()

    response = {
        "areas": AreaSerializer(areas, many=True).data,
        "localidades": LocalidadSerializer(localidades, many=True).data
    }

    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEmpleoById(request, pk):
    empleo = Empleo.objects.get(pk=pk)
    serializer = EmpleoSerializer(empleo)
    disabled = Postulacion.objects.filter(user=request.user, empleo=pk).exists()
    response = {
        "empleo": serializer.data,
        "disabled": disabled 
    }
    return Response(response)