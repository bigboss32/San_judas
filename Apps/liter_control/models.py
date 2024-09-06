from django.db import models

from Apps.production.models import ProducionDay



class Ruta(models.Model):
    data_register = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    name_route = models.CharField()


    def __str__(self):
        return self.name_route


class Provedor(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    data_register = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(null=True, blank=True,default="")
    second_name = models.CharField(null=True, blank=True,default="")
    last_name = models.CharField(null=True, blank=True,default="")
    second_last_name = models.CharField(null=True, blank=True,default="")
    cedula = models.IntegerField(null=True, blank=True)
    celular= models.BigIntegerField(null=True, blank=True)
    def nombre_completo(self):
        return f"{self.first_name} {self.second_name} {self.last_name} {self.second_last_name}"

    def __str__(self):
        return self.nombre_completo()


class RegisterDay(models.Model):
    provedor = models.ForeignKey(Provedor, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    producionday = models.ForeignKey(ProducionDay, on_delete=models.CASCADE)
    data_register = models.DateTimeField(auto_now_add=True)
    day = models.DateField(default=None, null=True, blank=True)
    liter = models.IntegerField(null=True, blank=True)
    value_liter = models.IntegerField(null=True, blank=True)
    adelantos = models.IntegerField(default=0)
    def __str__(self):
             if self.day is not None:
                 return self.day.strftime('%Y-%m-%d')
