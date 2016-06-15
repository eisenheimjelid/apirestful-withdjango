from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = ('nombre', 'descripcion', 'tipo', 'impuesto', 'factor',
            'cantidad', 'precio', 'subtotal')


class InfoFiscalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfoFiscal
        fields = ('tipo', 'nombre', 'rfc', 'email', 'telefono', 'calle',
            'noexterior', 'nointerior', 'colonia', 'municipio',
            'localidad','estado', 'observacion')


class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = ('solicitante', 'personas', 'detalle', 'subtotal',
            'impuestos', 'subtotal', 'total', 'uuid', 'serie', 'folio',
            'moneda', 'fecha')
