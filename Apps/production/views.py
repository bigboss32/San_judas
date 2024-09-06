from datetime import datetime, timedelta
from typing import Any
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib import messages


class RegisterProductionView(View):
    template_name = "production/registar_production.html"

    def __init__(self, **kwargs: Any) -> None:
       ...


    def get(self, request):
         dias_de_produccion = ProducionDay.objects.all().order_by('day')


         return render(
            request,
            self.template_name,
            {"dias_de_produccion":dias_de_produccion

            }

        )

    def post(self, request):
       cantidad = request.POST["Cantidad"]
       producto = request.POST["Producto"]
       fecha = request.POST["fecha"]
       dia_produccion=ProducionDay.objects.filter(name_producction=fecha)
       ProductionProducto.objects.create(
        producionday = dia_produccion.first(),
        producto = producto,
        cantidad=cantidad
       )
       messages.success(request, '¡La acción se completó exitosamente!')
       return redirect("registrar_production")
