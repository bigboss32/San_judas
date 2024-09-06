from django.db import models

class Ventas(models.Model):

    TIPOS_DE_ESTADOS_CHOICES = [
        ("Pagado", "pagado"),
        ("Debe", "debe"),

    ]
    cantidad = models.FloatField(null=True, blank=True)
    valor=models.IntegerField(null=True, blank=True)
    comprador = models.CharField(null=True, blank=True)
    estado = models.CharField(null=True, blank=True,choices=TIPOS_DE_ESTADOS_CHOICES)
    fecha_venta_incio=models.DateField(null=True, blank=True)
    fecha_venta_final=models.DateField(null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)
