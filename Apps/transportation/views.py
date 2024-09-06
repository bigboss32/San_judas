from datetime import datetime, timedelta
from typing import Any
from django.shortcuts import redirect, render
from django.views import View
from .models import RegisterDayTrasporte,Trasporte

from django.db.models import F, Sum
class TransportationView(View):
    template_name = "trasporte/trasporte.html"

    def __init__(self, **kwargs: Any) -> None:
       ...


    def get(self, request):
         # Obtener el nombre del conductor y realizar la multiplicación
       # Obtener el nombre del conductor y realizar la multiplicación para todas las rutas
        fecha_inicio = datetime(year=2024, month=3, day=1)
        fecha_fin = datetime(year=2024, month=3, day=15)
        resultados_por_conductor = RegisterDayTrasporte.objects.filter(
        registerday__day__range=(fecha_inicio, fecha_fin)  # Filtrar por rango de fechas
        ).values(
            'trasporte__conductor'  # Obtener el nombre del conductor
        ).annotate(
            total_litros_valen=Sum(F('value_liter_traspo') * F('registerday__liter')) ,
            total_a_pagar = Sum((F('value_liter_traspo') * (F('registerday__liter') - F('litros_no_llegaron'))) - F('adelantos')),
            total_litros=Sum( F('registerday__liter')) , # Sumar el resultado de la multiplicación
            total_litros_perdidos=Sum( F('litros_no_llegaron')) , # Sumar el resultado de la multiplicación
        )

        # Imprimir los resultados por conductor
        for resultado in resultados_por_conductor:
            print("Conductor:", resultado['trasporte__conductor'])
            print("Total de litros valor:", resultado['total_litros_valen'])
            print("Total de litros valor restando adelantos:", resultado['total_a_pagar'])
            print("Total de litros transportados:", resultado['total_litros'])
            print("Total de litros perdidos:", resultado['total_litros_perdidos'])

        return render(
            request,
            self.template_name,

        )
    def post (self, request):
        date_range = request.POST["range"].split(" - ")
        fecha_inicio_str, fecha_fin_str = date_range

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")

        resultados_por_conductor = RegisterDayTrasporte.objects.filter(
        registerday__day__range=(fecha_inicio, fecha_fin)  # Filtrar por rango de fechas
        ).values(
            'trasporte__conductor' ,
              'trasporte__ruta__name_route',# Obtener el nombre del conductor
              'value_liter_traspo'
        ).annotate(
            total_litros_valen=Sum(F('value_liter_traspo') * F('registerday__liter')) ,
            total_a_pagar = Sum((F('value_liter_traspo') * (F('registerday__liter') - F('litros_no_llegaron'))) - F('adelantos')),
            total_a_pagar_menosleche_perdida = Sum((F('value_liter_traspo') * (F('registerday__liter') - F('litros_no_llegaron')))),

            total_litros=Sum( F('registerday__liter')) , # Sumar el resultado de la multiplicación
            total_litros_perdidos=Sum( F('litros_no_llegaron')) , # Sumar el resultado de la multiplicación
            total_adelantos=Sum( F('adelantos')) ,

        )

        # Imprimir los resultados por conductor
        for resultado in resultados_por_conductor:
            print("Conductor:", resultado['trasporte__conductor'])
            print("Total de litros valor:", resultado['total_litros_valen'])
            print("Total de litros valor restando adelantos:", resultado['total_a_pagar'])
            print("Total de litros transportados:", resultado['total_litros'])
            print("Total de litros perdidos:", resultado['total_litros_perdidos'])

        return render(
            request,
            self.template_name,
             {
                "resultados_por_conductor": resultados_por_conductor,

            },

        )
