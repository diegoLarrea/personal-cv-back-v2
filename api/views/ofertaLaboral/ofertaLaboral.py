from api.models import OfertaLaboral, Nivel, Dominio, Localidad, Area
from api.serializers.ofertaLaboral.ofertaLaboralSerializer import OfertaLaboralSerializer 
from api.serializers.ajustes.ajustes import NivelSerializer, LocalidadSerializer, DominioSerializer, AreaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from rest_framework.permissions import IsAuthenticated

class ofertaList(APIView):
    """
    Lista todas las ofertas, o crea una nueva oferta.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # Get all data
        ofertas = OfertaLaboral.objects.all()
        
        # Query Params
        page = request.GET.get('page', 1)
        itemsPP = request.GET.get('cantidad', 10)
        orderBy = request.GET.get('orderBy', "fecha_creacion")
        orderDir = request.GET.get('orderDir', "-")
        oportunidad = request.GET.get("oportunidad", None)  
        filters = request.GET.get('filters', None)
        
        if filters is not None:
            filters = json.loads(filters)
        
        areas_ids = filters.get("areas", None)
        localidades_ids = filters.get("localidades", None)

        array_areas_ids = []
        if areas_ids is not None:
            for i in areas_ids:
                array_areas_ids.append(i["id"])

        array_localidades_ids = []
        if localidades_ids is not None:
            for i in localidades_ids:
                array_localidades_ids.append(i["id"])

        if array_areas_ids:
            ofertas = ofertas.filter(area__in=array_areas_ids)

        if array_localidades_ids:
            ofertas = ofertas.filter(localidad__in=array_localidades_ids)
        
        if oportunidad is not None:
            print(oportunidad)
            ofertas = ofertas.filter(oportunidad__contains=oportunidad)
        
        ofertas = ofertas.order_by("%s%s" % (orderDir, orderBy))

        paginator = Paginator(ofertas, itemsPP)
        ofertasLaborales = paginator.page(page)
        items = []

        for f in ofertasLaborales:
            items.append(
                {
                    "oportunidad": f.oportunidad,
                    "descripcion": f.descripcion,
                    "requisitos": f.requisitos,
                    "tipo": f.tipo,
                    "vigencia": f.vigencia,
                    "localidad": LocalidadSerializer(f.localidad).data,
                    "nivel": NivelSerializer(f.nivel).data,
                    "area": AreaSerializer(f.area).data,
                    "dominio": DominioSerializer(f.dominio).data,
                    "fecha_creacion": f.fecha_creacion
                }
            )
        response = {
            "items" : items,
            "total": ofertas.count()
        }
        return Response(response)


    def post(self, request, format=None):
        serializer = OfertaLaboralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ofertaDetail(APIView):
    """
    Retrieve, update or delete a oferta instance.
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return OfertaLaboral.objects.get(pk=pk)
        except OfertaLaboral.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        oferta = self.get_object(pk)
        serializer = OfertaLaboralSerializer(oferta)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        oferta = self.get_object(pk)
        serializer = OfertaLaboralSerializer(oferta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        oferta = self.get_object(pk)
        oferta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)