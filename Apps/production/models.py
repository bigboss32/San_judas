from django.db import models

from Apps.liter_control.models import *


class ProducionDay(models.Model):
    day = models.DateField(default=None, null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)
    name_producction = models.CharField(null=True, blank=True)

    class Meta:
        unique_together = ("data_register", "name_producction")


class ProductionProducto(models.Model):
    data_register = models.DateTimeField(auto_now_add=True)
    producionday = models.ForeignKey(ProducionDay, on_delete=models.CASCADE)
    producto = models.CharField(null=True, blank=True)
    cantidad=models.FloatField(null=True, blank=True)
