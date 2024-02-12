from django.db import models


class Rol(models.Model):
    name = models.CharField(null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)


class RegisterDayEmploy(models.Model):
    name = models.CharField(null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)


class Empleado(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    data_register = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(null=True, blank=True)
    second_name = models.CharField(null=True, blank=True)
    last_name = models.CharField(null=True, blank=True)
    second_last_name = models.CharField(null=True, blank=True)
    cedula = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField(null=True, blank=True)
    total_dias = models.BigIntegerField(null=True, blank=True)
    valor_del_dia = models.IntegerField(null=True, blank=True)
    adelantos = models.IntegerField(null=True, blank=True)
    anexos = models.IntegerField(null=True, blank=True)
    valor_total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name
