from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from api.serializers.user.userSerializer import UserSerializer
from api.serializers.persona.personaSerializer import PersonaSerializer
from api.models import Persona
from django.core.paginator import Paginator
import json
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class userList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        users = Persona.objects.all()

        page = request.GET.get('page', 1)
        itemsPP = request.GET.get('cantidad', 10)
        orderBy = request.GET.get('orderBy', "nombres")
        orderDir = request.GET.get('orderDir', "ASC")
        search = request.GET.get("search", None)
        
        if search is not None:

            search = json.loads(search)
            
            nombres = search.get("nombres") 
            apellidos = search.get("apellidos")
            documento = search.get("documento")
            email = search.get("email") 
            pais = search.get("pais")
            ciudad = search.get("ciudad")
            fecha_nacimiento = search.get("fecha_nacimiento")

            if nombres is not None:
                users =  users.filter(nombres__icontains= nombres)

            if apellidos is not None:
                users =  users.filter(apellidos__icontains= apellidos)
        
            if documento is not None:
                users =  users.filter(documento__icontains= documento)

            if email is not None:
                users =  users.filter(email__icontains= email)

            if pais is not None:
                users = users.filter(pais_nacimiento__icontains= pais)

            if ciudad is not None:
                users = users.filter(ciudad_residencia__icontains = ciudad)

            if fecha_nacimiento is not None:
                users = users.filter(fecha_nacimiento__icontains = fecha_nacimiento)
            
        if orderDir == "ASC":
            orderDir=""
        else:
            orderDir="-"

        users = users.order_by("%s%s" % (orderDir, orderBy))

        paginator = Paginator(users, itemsPP)
        usuarios = paginator.page(page)

        serializer = PersonaSerializer(usuarios, many=True)
        response = {
            "items": serializer.data,
            "total": users.count()
        }
        return Response(response)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
