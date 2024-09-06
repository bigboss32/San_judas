from django.db import models

from Apps.production.models import ProducionDay


class Gastos(models.Model):

    TIPOS_DE_GASTO_CHOICES = [
        ("leche", "Leche"),
        ("transporte", "Transporte"),
        ("empleados", "Empleados"),
        ("transporte_queso", "Transporte Queso"),
        ("flete_queso", "Flete Queso"),
        ("cuajador_mirolindo", "Cuajador Mirolindo"),
        ("sal", "Sal"),
        ("varios", "Varios"),
        ("jabon", "Jabón"),
        ("cuajo", "Cuajo"),
        ("energia", "Energía"),
        ("bolsas", "Bolsas"),
        ("cloro", "Cloro"),
    ]
    tipo_de_gasto = models.CharField(
        null=True, blank=True, choices=TIPOS_DE_GASTO_CHOICES
    )
    descripcion = models.CharField(null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)
    day = models.DateField(default=None, null=True, blank=True)
