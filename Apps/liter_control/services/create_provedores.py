from django.http import HttpResponse
from Apps.liter_control.models import Provedor,Ruta
class CrudProvedores:
    def create_provedores(self,request):
        primernombre = request.POST['primernombre']
        segundornombre = request.POST['segundornombre']
        primerapellido = request.POST['primerapellido']
        segundopellido = request.POST['segundopellido']
        cedula = request.POST['cedula']
        rutas_id = request.POST['rutas_id']
        rutas=Ruta.objects.get(id=rutas_id)

        proveedor = Provedor.objects.create(
            ruta=rutas,
            first_name=primernombre,
            second_name=segundornombre,
            last_name=primerapellido,
            second_last_name=segundopellido,
            cedula=cedula
        )

        if proveedor:
            return True
        else:
            return False
