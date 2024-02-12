import locale
from calendar import month_name
from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import ExtractMonth, TruncMonth
from django.shortcuts import render
from django.views import View

from Apps.liter_control.models import Provedor, RegisterDay, Ruta
from Apps.transportation.models import Automovil


class Indexview(View):
    template_name = "main.html"

    def get(self, request):

        total_provedores = Provedor.objects.count()
        total_ruta = Ruta.objects.count()
        total_automoviles = Automovil.objects.count()
        ahora = datetime.now()
        mes_actual = ahora.month
        año_actual = ahora.year
        total_litros_leche_mes_actual = RegisterDay.objects.filter(
            day__month=mes_actual, day__year=año_actual
        ).aggregate(total_litros=Sum("liter"))["total_litros"]
        litros_por_mes = (
            RegisterDay.objects.annotate(mes=TruncMonth("day"))
            .values("mes")
            .annotate(nombre_mes=ExtractMonth("mes"), total_litros=Sum("liter"))
        )

        # Mapea el número del mes al nombre del mes en español
        meses_espanol = {
            1: "Enero",
            2: "Febrero",
            # ... Agrega los demás meses según sea necesario
        }

        for mes in litros_por_mes:
            mes["nombre_mes"] = meses_espanol.get(mes["nombre_mes"], "Desconocido")
            print(litros_por_mes)
        return render(
            request,
            self.template_name,
            {
                "total_provedores": total_provedores,
                "total_ruta": total_ruta,
                "total_automoviles": total_automoviles,
            },
        )

    def post(self, request): ...
