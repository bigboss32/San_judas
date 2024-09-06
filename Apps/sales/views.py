from datetime import datetime, timedelta
from typing import Any
from django.shortcuts import redirect, render
from django.views import View
from .models import Ventas

class RegisterSalesView(View):
    template_name = "registar_ventas/registar_ventas.html"

    def __init__(self, **kwargs: Any) -> None:
       ...


    def get(self, request):


         return render(
            request,
            self.template_name,

        )

    def post(self, request):

        cantidad = request.POST["Cantidad"]
        valor = request.POST["Valor"]
        comprador = request.POST["Comprador"]
        estado = request.POST["estado"]
        date_range = request.POST["range"].split(" - ")
        fecha_inicio_str, fecha_fin_str = date_range

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
        Ventas.objects.create(cantidad=cantidad,valor=valor,comprador=comprador,estado=estado,fecha_venta_incio=fecha_inicio,fecha_venta_final=fecha_fin

        )
        return redirect("registrar_ventas")
