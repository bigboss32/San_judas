from typing import Any
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from . models import Gastos
from Apps.bills.services.obtener_gastos import GetBills


class BillsView(View):
    template_name = "gasto/registar_gasto.html"

    def __init__(self, **kwargs: Any) -> None:
        pass

    def get(self, request):
        return GetBills.obtener_gastos(request, self.template_name)

    def post(self, request):
        Valor = request.POST["Valor"]
        Dia = request.POST["Dia"]
        gastos = request.POST["gastos"]
        descrip = request.POST["descrip"]
        cantidad = request.POST["cantidad"]

        Gastos.objects.create(
            tipo_de_gasto=gastos,
            descripcion=descrip,
            valor=Valor,
            day=Dia,
            cantidad=cantidad
        )

        messages.success(request, f"registro con éxito.")


        return redirect('registrar_gastos')
