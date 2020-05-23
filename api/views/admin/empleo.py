from api.models import Empleo
from api.serializers.empleo.empleoSerializer import EmpleoSerializer, EmpleoAdminSerializer
from api.serializers.empleo.postulacionSerializer import PostulantesSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from hashids import Hashids
from django.db.models import Q
import json

class empleoList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
            
        ofertas = Empleo.objects.all()

        # Query Params
        page = request.GET.get('page', 1)
        itemsPP = request.GET.get('cantidad', 10)
        orderBy = request.GET.get('orderBy', "fecha_creacion")
        orderDir = request.GET.get('orderDir', "-")
        filters = request.GET.get('filters', None)

        if filters is not None:
            filters = json.loads(filters)
            areas_json = filters.get("areas", None)
            localidades_json = filters.get("localidades", None)
            search = filters.get("search", None)

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

            if search is not None:
                ofertas = ofertas.filter(Q(codigo=search) | Q(oportunidad__icontains=search))

        if orderDir == "ASC":
            orderDir=""
        else:
            orderDir="-"

        ofertas = ofertas.order_by("%s%s" % (orderDir, orderBy))

        paginator = Paginator(ofertas, itemsPP)
        empleos = paginator.page(page)

        serializer = EmpleoSerializer(empleos, many=True)
        
        response = {
            "items": serializer.data,
            "total": ofertas.count()
        }
        return Response(response)

    def post(self, request, format=None):
        serializer = EmpleoAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            obj = Empleo.objects.get(pk=serializer.data.get("id"))
            hashids = Hashids(min_length=4) 
            obj.codigo = hashids.encode(obj.id)
            obj.save()
            s = EmpleoAdminSerializer(obj)
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class empleoDetail(APIView):
   
    def get_object(self, pk):
        try:
            return Empleo.objects.get(pk=pk)
        except Empleo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        empleo = self.get_object(pk)
        serializer = EmpleoAdminSerializer(empleo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        empleo = self.get_object(pk)
        serializer = EmpleoAdminSerializer(empleo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        empleo = self.get_object(pk)
        empleo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

