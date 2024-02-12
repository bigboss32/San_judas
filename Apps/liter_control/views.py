from datetime import date
from typing import Any

from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from Apps.base.services.crearte_register_day import CreateRegister
from Apps.liter_control.models import RegisterDay

from .services.create_provedores import *
from .services.create_rutas import *


class CrearProvedoresView(View):
    template_name = "provedores/crear_provedor.html"

    def __init__(self, **kwargs: Any) -> None:
        self.crudprovedores = CrudProvedores()
        self.crudrutas = CrudRutas()

    def get(self, request):
        rutas = self.crudrutas.get_rutas()
        return render(request, self.template_name, {"ruta": rutas})

    def post(self, request):

        provedor = self.crudprovedores.create_provedores(request)
        if provedor:
            messages.success(request, f"registro con éxito.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

        return render(request, self.template_name)


class ObtenerProvedores(View):
    template_name = "provedores/info_provedor.html"

    def __init__(self, **kwargs: Any) -> None:
        self.crudrutas = CrudRutas()

    def get(self, request):
        provedor = Provedor.objects.all()
        tu_mes = 3
        ano_actual = timezone.now().year
        fecha_filtro = date(year=2024, month=1, day=1)

        litros_por_proveedor = (
            RegisterDay.objects.filter(
                day__month=fecha_filtro.month, day__year=fecha_filtro.year
            )
            .values(
                "provedor__first_name",
                "provedor__second_name",
                "provedor__last_name",
                "provedor__second_last_name",
                "provedor__cedula",
                "ruta__name_route",
            )
            .annotate(
                total_litros=Sum("liter"),
                total_adelantos=Sum("adelantos"),
                value_total_adelantos=Sum("value_total_adelantos"),
            )
        )
        total_provedores = Provedor.objects.count()
        total_litros_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_litros_en_toda_la_consulta=Sum("total_litros")
        )["total_litros_en_toda_la_consulta"]
        total_adelantos_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_adelantos_en_toda_la_consulta=Sum("total_adelantos")
        )["total_adelantos_en_toda_la_consulta"]
        total_total_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_total_en_toda_la_consulta=Sum("value_total_adelantos")
        )["total_total_en_toda_la_consulta"]
        return render(
            request,
            self.template_name,
            {
                "litros_por_proveedor": litros_por_proveedor,
                "total_provedores": total_provedores,
                "total_litros_en_toda_la_consulta": total_litros_en_toda_la_consulta,
                "total_adelantos_en_toda_la_consulta": total_adelantos_en_toda_la_consulta,
                "total_total_en_toda_la_consulta": total_total_en_toda_la_consulta,
            },
        )


class CrearRutasView(View):
    template_name = "rutas/crear_rutas.html"

    def __init__(self, **kwargs: Any) -> None:
        self.crudrutas = CrudRutas()

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        rutas = self.crudrutas.create_rutas(request)
        if rutas:
            messages.success(request, f"registro con éxito.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

        return render(request, self.template_name)


class SelectRutaView(View):
    template_name = "rutas/seleccionar_rutas.html"

    def __init__(self, **kwargs: Any) -> None:
        self.crudrutas = CrudRutas()

    def get(self, request):
        rutas = self.crudrutas.get_rutas()
        return render(request, self.template_name, {"ruta": rutas})


class LiterDayView(View):
    template_name = "registro_diario/registro_diario.html"

    def __init__(self, **kwargs: Any) -> None:
        self.crudrutas = CrudRutas()
        self.createregister = CreateRegister()

    def get(self, request, ruta_id):
        return self.createregister.get_rutas(request, ruta_id, self.template_name)

    def post(self, request, ruta_id):
        return self.createregister.createregisterday(request, ruta_id)
