from django.contrib import admin

from .models import *

@admin.register(Provedor)
class ProvedorAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

@admin.register(RegisterDay)
class RegisterDayAdmin(admin.ModelAdmin):
    list_display = ('provedor',)

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('name_route',)