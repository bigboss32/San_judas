from django.db import models

from Apps.transportation.models import *
from Apps.production.models import ProducionDay

class Ruta(models.Model):
    data_register=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField()
    name_route= models.CharField()

class Provedor(models.Model):
    ruta= models.ForeignKey(Ruta, on_delete=models.CASCADE)
    data_register=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField()
    second_name=models.CharField()
    last_name=models.CharField()
    second_last_name=models.CharField()
    cedula=models.IntegerField()
   

class RegisterDay(models.Model):
    provedor= models.ForeignKey(Provedor, on_delete=models.CASCADE)
    trasporte= models.ForeignKey(Trasporte, on_delete=models.CASCADE)
    ruta= models.ForeignKey(Ruta, on_delete=models.CASCADE)
    producionday= models.ForeignKey(ProducionDay, on_delete=models.CASCADE)
    data_register=models.DateTimeField(auto_now_add=True)
    day = models.DateField(default=None, null=True, blank=True)
    liter=models.IntegerField()
    value_liter=models.IntegerField()
    adelantos = models.IntegerField(default=0)
    value_total=models.IntegerField(null=True, blank=True)
    value_total_adelantos=models.IntegerField(null=True, blank=True)
    
