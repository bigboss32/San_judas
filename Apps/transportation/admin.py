from django.contrib import admin
from .models import *

@admin.register(Trasporte)
class TrasporteAdmin(admin.ModelAdmin):
    list_display = ("conductor","ruta")


@admin.register(RegisterDayTrasporte)
class TrasporteAdmin(admin.ModelAdmin):
    list_display = ("trasporte","registerday","adelantos","get_provedor","value_liter_traspo")
    search_fields = ['registerday__provedor__first_name',"trasporte__conductor"]

    def get_provedor(self, obj):
        return obj.registerday.provedor.first_name  # Reemplaza 'nombre' con el nombre del campo que deseas mostrar

    get_provedor.short_description = 'Proveedor'  # Esto establece el encabezado de la columna en el admin
