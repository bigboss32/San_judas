from django.db.models import Count
from django.http import HttpResponse

from Apps.liter_control.models import Ruta


class CrudRutas:
    def create_rutas(self, request):
        nombreruta = request.POST["nombreruta"]
        estado = request.POST.get("estado", False)
        if estado == "on":
            estado = True
        ruta = Ruta.objects.create(status=estado, name_route=nombreruta)

        if ruta:
            return True
        else:
            return False

    def get_rutas(self):
        rutas = Ruta.objects.annotate(num_proveedores=Count("provedor"))
        return rutas
