from django.db import models
from Apps.liter_control.models import Provedor

class DeudaProveedor(models.Model):
    provedor=models.ForeignKey(Provedor, on_delete=models.CASCADE)
    data_register = models.DateTimeField(auto_now_add=True)
    fecha_deuda= models.CharField(null=True, blank=True,)
    valor_total_deuda = models.BigIntegerField(null=True, blank=True,default=0)
