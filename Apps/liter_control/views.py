from datetime import datetime, timedelta
from typing import Any
from django.db.models import Sum, F
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render,redirect
from django.utils import timezone
from django.views import View

from Apps.base.services.crearte_register_day import CreateRegister
from Apps.liter_control.models import RegisterDay
from Apps.transportation.models import RegisterDayTrasporte
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

        return redirect('crearprovedores')


class ObtenerProvedores(View):
    template_name = "provedores/info_provedor.html"

    def __init__(self, **kwargs: Any) -> None:
        self.crudrutas = CrudRutas()

    def get(self, request):
        fecha_inicio = datetime(year=2024, month=3, day=10)
        fecha_fin = datetime(year=2024, month=3, day=10)

        litros_por_proveedor = (
            RegisterDay.objects.filter(
                day__range=(fecha_inicio, fecha_fin)
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

            )
        )
        total_provedores = Provedor.objects.count()
        total_litros_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_litros_en_toda_la_consulta=Sum("total_litros")
        )["total_litros_en_toda_la_consulta"]
        total_adelantos_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_adelantos_en_toda_la_consulta=Sum("total_adelantos")
        )["total_adelantos_en_toda_la_consulta"]

        return render(
            request,
            self.template_name,
            {
                "litros_por_proveedor": litros_por_proveedor,
                "total_provedores": total_provedores,
                "total_litros_en_toda_la_consulta": total_litros_en_toda_la_consulta,
                "total_adelantos_en_toda_la_consulta": total_adelantos_en_toda_la_consulta,

            },
        )
    def post (self, request):

        date_range = request.POST["range"].split(" - ")
        fecha_inicio_str, fecha_fin_str = date_range

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
        litros_por_proveedor = (
            RegisterDay.objects.filter(
                day__range=(fecha_inicio, fecha_fin),

            )
            .values(
                "provedor__first_name",
                "provedor__second_name",
                "provedor__last_name",
                "provedor__second_last_name",
                "provedor__cedula",
                "ruta__name_route",
                "value_liter",
                "liter"
            )
            .annotate(
                total_litros=Sum("liter"),
                total_adelantos=Sum("adelantos"),
                monto_total_litros=F("value_liter") * Sum("liter")

            )
        )
        peuiwb=0
        for registro in litros_por_proveedor:
            proveedor_nombre = f"{registro['provedor__first_name']} {registro['provedor__second_name']} {registro['provedor__last_name']} {registro['provedor__second_last_name']}"
            cedula_proveedor = registro['provedor__cedula']
            ruta = registro['ruta__name_route']
            total_litros = registro['total_litros']
            total_adelantos = registro['total_adelantos']
            monto_total_litros = registro['monto_total_litros']
            peuiwb+=total_litros



        total_provedores = Provedor.objects.count()
        total_litros_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_litros_en_toda_la_consulta=Sum("total_litros")
        )["total_litros_en_toda_la_consulta"]
        total_adelantos_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_adelantos_en_toda_la_consulta=Sum("total_adelantos")
        )["total_adelantos_en_toda_la_consulta"]
        total_total_en_toda_la_consulta = litros_por_proveedor.aggregate(
            total_total_en_toda_la_consulta=Sum("monto_total_litros")
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

class LiterUpdate(View):
     template_name = "registro_diario/actualizar_registro.html"
     def __init__(self, **kwargs: Any) -> None:
        self.crudrutas = CrudRutas()
        self.createregister = CreateRegister()
     def get(self, request):
        rutas = self.crudrutas.get_rutas()

        alls=RegisterDayTrasporte.objects.filter(trasporte__conductor="propio")
        for all in alls:
            all.value_liter_traspo=0
            all.save()
        return render(request, self.template_name, {"ruta": rutas})
     def post(self, request):

        date_range = request.POST["date_range"].split(" - ")
        id_ruta = request.POST["rutas_id"]
        valor = request.POST["valor"]
        fecha_inicio_str, fecha_fin_str = date_range

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
        rutas=Ruta.objects.get(id=id_ruta)
        registros = RegisterDay.objects.filter(day__range=(fecha_inicio, fecha_fin),ruta=rutas)
        for registro in registros:
          registro.value_liter=valor
          registro.save()
        r=RegisterDay.objects.filter(provedor__first_name="Livardo Rivera",day__range=(fecha_inicio, fecha_fin)
                                    )
        for registro in r:
          registro.value_liter=1800
          registro.save()
        r=RegisterDay.objects.filter(provedor__first_name="Henri",day__range=(fecha_inicio, fecha_fin)
                                    )
        for registro in r:
          registro.value_liter=1500
          registro.save()
        return redirect('actualizar_valor_litros')
