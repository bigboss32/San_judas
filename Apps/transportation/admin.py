from django.contrib import admin

from .models import *


@admin.register(Trasporte)
class TransporteAdmin(admin.ModelAdmin):
    list_display = ("empleado", "automovil", "registerdaytrasport", "data_register")


@admin.register(Automovil)
class AutomovilAdmin(admin.ModelAdmin):
    list_display = ("tipo", "placa", "color", "estado")


@admin.register(RegisterDayTrasport)
class RegisterDayTrasportAdmin(admin.ModelAdmin):
    list_display = ("day",)
