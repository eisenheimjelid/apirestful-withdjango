from django.contrib.auth.models import User
from django.db import models


CONTACT_TYPES = (
    ('Emisor', 'Emisor'),
    ('Receptor', 'Receptor'),
)


# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=1024, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=False)
    tipo = models.CharField(max_length=128, null=True, blank=True)
    impuesto = models.CharField(max_length=4, null=True, blank=True)
    factor = models.DecimalField(default=0.16, max_digits=19, decimal_places=2)
    cantidad = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4, null=True, blank=True)

    class Meta:  # Metadata
        app_label = 'api'
        ordering = ["id"]
        verbose_name = "concepto"
        verbose_name_plural = "conceptos"

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre


class InfoFiscal(models.Model):
    tipo = models.CharField(max_length=32, choices=CONTACT_TYPES)
    nombre = models.CharField(max_length=512, null=True, blank=True)
    rfc = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=1024, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    calle = models.CharField(max_length=512, null=True, blank=True)
    noexterior = models.CharField(max_length=32, null=True, blank=True)
    nointerior = models.CharField(max_length=32, null=True, blank=True)
    colonia = models.CharField(max_length=512, null=True, blank=True)
    municipio = models.CharField(max_length=512, null=True, blank=True)
    localidad = models.CharField(max_length=512, null=True, blank=True)
    estado = models.CharField(max_length=512, null=True, blank=True)
    observacion = models.TextField(null=True, blank=True)
 
    class Meta:  # Metadata
        app_label = 'api'
        ordering = ["id"]
        verbose_name = "informacion Fiscal"
        verbose_name_plural = "informaciones Fiscales"
 
    def __str__(self):              # __unicode__ on Python 2
        return self.rfc


class Factura(models.Model):
    solicitante = models.ForeignKey(User, null=True, blank=True)
    personas =  models.ManyToManyField("InfoFiscal", blank=True)
    detalle =  models.ManyToManyField("Servicio", blank=True)
    impuestos = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    uuid = models.CharField(max_length=48, null=True, blank=True)
    serie = models.CharField(max_length=50, null=True, blank=True)
    folio = models.CharField(default='00' ,max_length=100, null=True, blank=True)
    moneda = models.CharField(max_length=10, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
 
 
    class Meta:  # Metadata
        app_label = 'api'
        ordering = ["id"]
        verbose_name = "factura"
        verbose_name_plural = "facturas"
 
    def __str__(self):              # __unicode__ on Python 2
        return self.folio
    
    def getSolicitante(self):              # __unicode__ on Python 2
        return self.solicitante.username
