from django.db import models

from Apps.employees.models import *


class Automovil(models.Model):
    tipo = models.CharField(null=True, blank=True)
    placa = models.CharField(null=True, blank=True)
    color = models.CharField(null=True, blank=True)
    estado = models.CharField(null=True, blank=True)


class RegisterDayTrasport(models.Model):
    valor = models.IntegerField(null=True, blank=True)
    trabajo = models.BooleanField(default=True)
    day = models.DateField(default=None, null=True, blank=True)


class Trasporte(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE)
    registerdaytrasport = models.ForeignKey(
        RegisterDayTrasport, on_delete=models.CASCADE
    )
    data_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empleado.first_name
