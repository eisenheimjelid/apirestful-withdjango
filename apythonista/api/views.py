from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets
from api.serializers import *
from api.models import *


def postPersonalizado(request):
    """ api/personalizado/ """
    contenido = {
        'recibido': request.data
    }
    return HttpResponse(JsonResponse(contenido).content,
        content_type="application/json", status=200)


def notImplemented(request):
    """ 501 Not Implemented """
    contenido = {
        'error': "Not Implemented"
    }
    return HttpResponse(JsonResponse(contenido).content,
        content_type="application/json", status=501)



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


class Personalizado(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    parser_handler = (JSONParser, )
    def get(self, request, format=None):
        return notImplemented(request)

    def post(self, request, format=None):
        return postPersonalizado(request)
