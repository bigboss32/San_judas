from datetime import datetime, timezone

from django.utils import timezone

from Apps.liter_control.models import *
from Apps.production.models import ProducionDay
from Apps.transportation.models import Trasporte,RegisterDayTrasporte


class Database:
    def create_register_day(self, data):
        provedor = Provedor.objects.get(id=data["id"])
        ruta = Ruta.objects.get(id=data["ruta_id"])
        producionday = ProducionDay.objects.filter(day=data["fecha"]).first()
        if not producionday:
            producionday = ProducionDay.objects.create(
                day=data["fecha"], name_producction=data["fecha"]
            )

        registerday=RegisterDay.objects.create(
            provedor=provedor,
            ruta=ruta,
            producionday=producionday,
            day=data["fecha"],
            liter=data["litros"],
            value_liter=data["valor_litro"],
            adelantos=data["avances"],
        )
        return registerday

    def obtener_provedor(self, ruta_id,request):

           # Filtrar los proveedores por la ruta específica
            proveedores_por_ruta = Provedor.objects.filter(ruta=ruta_id)
            fecha=request.GET.get('fecha')
            if request.GET.get('fecha') is None:
                 fecha=timezone.localtime(timezone.now())


            # Obtener los IDs de los proveedores que tienen un RegisterDay en la fecha especificada y para la ruta específica
            ids_proveedores_con_registerday = RegisterDay.objects.filter(day=fecha, ruta=ruta_id).values_list('provedor_id', flat=True)

            # Excluir los proveedores que tienen un RegisterDay en la fecha especificada y para la ruta específica
            proveedores_sin_registerday = proveedores_por_ruta.exclude(id__in=ids_proveedores_con_registerday)

            return proveedores_sin_registerday

    def obtener_trasporte(self,ruta_id):
        rutas= Ruta.objects.get(id=ruta_id)
        trasportes_hoy = Trasporte.objects.get(ruta=rutas)


        return trasportes_hoy
    def create_register_day_trasport(self, data,registerday):
         trasporte= Trasporte.objects.get(id=data["id_trasporte"])
         RegisterDayTrasporte.objects.create(
              trasporte=trasporte,
              registerday=registerday,
              value_liter_traspo=data["Valor_tras"],
              litros_no_llegaron=data["Litros_eli"]

         )
