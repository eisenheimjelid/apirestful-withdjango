from django.contrib import admin
from api.models import *

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'cantidad', 'precio', 'subtotal')
    list_display_links = ('id', 'nombre')


class InfoFiscalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rfc', 'email', 'telefono', 'tipo')
    list_display_links = ('id', 'nombre', 'rfc', 'email')


class FacturaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'uuid', 'serie', 'folio', 'getSolicitante')
    list_display_links = ('fecha', 'uuid', 'serie', 'folio')


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(InfoFiscal, InfoFiscalAdmin)
admin.site.register(Factura, FacturaAdmin)
