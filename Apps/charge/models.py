from django.db import models



class Turbo(models.Model):
    data_register = models.DateTimeField(auto_now_add=True)
    conductor=models.CharField(null=True, blank=True)
    cedula=models.IntegerField(null=True, blank=True)
    turbo=models.CharField(null=True, blank=True)

class Flete(models.Model):
    dia_inicio= models.DateField(default=None, null=True, blank=True)
    dia_final=models.DateField(default=None, null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)

class GanaciasFlete(models.Model):
    turbo=models.ForeignKey(Turbo, on_delete=models.CASCADE, default=None)
    flete = models.ForeignKey(Flete, on_delete=models.CASCADE, default=None)

    day = models.DateField(default=None, null=True, blank=True)
    valor=models.IntegerField(null=True, blank=True)
    cantidad=models.FloatField(null=True, blank=True)
    name= models.CharField(null=True, blank=True)
    descripcion=models.CharField(null=True, blank=True)
    data_register = models.DateTimeField(auto_now_add=True)


class GastosCarro(models.Model):
    flete = models.ForeignKey(Flete, on_delete=models.CASCADE, default=None)

    turbo=models.ForeignKey(Turbo, on_delete=models.CASCADE, default=None)
    data_register = models.DateTimeField(auto_now_add=True)
    valor=models.IntegerField(null=True, blank=True)
    cantidad=models.FloatField(null=True, blank=True)
    name= models.CharField(null=True, blank=True)
    descripcion=models.CharField(null=True, blank=True)
