from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from api.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    Servicio API para visualizar o editar a los usuarios del sistema
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Servicio API para visualizar o editar a los grupos del sistema
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    """
    Servicio API para visualizar todos los servicios
    """
    queryset = Servicio.objects.filter(activo=True)
    serializer_class = ServicioSerializer


class InfoFiscalViewSet(viewsets.ModelViewSet):
    """
    Servicio API para visualizar todo el listado de personas
    """
    queryset = InfoFiscal.objects.all()
    serializer_class = InfoFiscalSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    """
    Servicio API para visualizar todas las facturas
    """
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
