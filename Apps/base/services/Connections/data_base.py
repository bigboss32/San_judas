from datetime import timezone, datetime
from datetime import datetime
from django.utils import timezone
from Apps.liter_control.models import *
from Apps.transportation.models import *
from Apps.production.models import ProducionDay
class Database():
    def create_register_day(self,data):
            provedor=Provedor.objects.get(id=data["id"])
            ruta=Ruta.objects.get(id=data["ruta_id"])
            trasporte=Trasporte.objects.get(id=data["trasporte"])
            producionday=ProducionDay.objects.filter(day=data["fecha"]).first()
            if not producionday:
                 producionday=ProducionDay.objects.create(
                         day=data["fecha"],
                         name_producction = f"Tanda-{data["fecha"]}"
                      
                 )
            
            RegisterDay.objects.create(
                provedor= provedor,
                ruta= ruta,
                trasporte=trasporte,
                producionday=producionday,
                day = data["fecha"],
                liter=data["litros"],
                value_liter=data["valor_litro"],
                adelantos =data["avances"],
                value_total=data["total"],
                value_total_adelantos=data["total_adelanto"]
                
            )
    def obtener_provedor(self,ruta_id):
        provedor=Provedor.objects.filter(ruta=ruta_id)
        return provedor
    def obtener_trasporte(self):
      
        hoy = timezone.localtime(timezone.now())
        trasportes_hoy = Trasporte.objects.filter(registerdaytrasport__day=hoy.date())
    
        return trasportes_hoy

         