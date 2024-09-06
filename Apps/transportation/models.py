from django.db import models
from Apps.liter_control.models import RegisterDay,Ruta

class Trasporte(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE,default=0)
    conductor=models.CharField(null=True, blank=True,)
    cedula=models.CharField(null=True, blank=True,)
    automovil=models.CharField(null=True, blank=True,)
    data_register = models.DateTimeField(auto_now_add=True)


    def __str__(self):
            return self.conductor

class RegisterDayTrasporte(models.Model):
    trasporte = models.ForeignKey(Trasporte, on_delete=models.CASCADE)
    registerday = models.ForeignKey(RegisterDay, on_delete=models.CASCADE)
    data_register = models.DateTimeField(auto_now_add=True)
    value_liter_traspo = models.IntegerField(null=True, blank=True)
    litros_no_llegaron= models.IntegerField(null=True, blank=True,default=0)
    adelantos = models.IntegerField(default=0)
