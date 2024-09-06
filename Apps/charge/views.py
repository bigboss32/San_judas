from datetime import datetime, timedelta
from typing import Any
from django.shortcuts import redirect, render
from django.views import View
from .models import GastosCarro, Turbo,GanaciasFlete,Flete
from django.contrib import messages
from django.db.models import F, Sum
class TurboView(View):
    template_name = "reports_turbo.html"

    def __init__(self, **kwargs: Any) -> None:
       ...


    def get(self, request):
        total_gastos_por_flete = Flete.objects.annotate(
        total_gastos=Sum(F('gastoscarro__valor') * F('gastoscarro__cantidad'))
)


        total_ganacia = Flete.objects.annotate(
        total_gastos=Sum(F('ganaciasflete__valor') * F('ganaciasflete__cantidad'))
)



        return render(
            request,
            self.template_name,
            {"total_gastos_por_flete":total_gastos_por_flete,
             "total_ganacia":total_ganacia}


        )

    def post(self, request):


        return redirect("registrar_ventas")



class RegisterTravelsView(View):
    template_name = "turbo_registro.html"

    def __init__(self, **kwargs: Any) -> None:
       ...


    def get(self, request):
        turbos=Turbo.objects.all()




        return render(
            request,
            self.template_name,
            {
                "turbos":turbos
            }

        )

    def post(self, request):
        date_range = request.POST["date_range"].split(" - ")
        valor = request.POST["valor"]
        Cantidad = request.POST["Cantidad"]
        Descripcion = request.POST["Descripcion"]
        conductores_id = request.POST["conductores_ids"]
        fecha_inicio_str, fecha_fin_str = date_range

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
        nuevo_flete = Flete.objects.filter(dia_inicio__lte=fecha_inicio, dia_final__gte=fecha_fin).first()

        if not nuevo_flete:

            nuevo_flete = Flete.objects.create(dia_inicio=fecha_inicio, dia_final=fecha_fin)


        tubro=Turbo.objects.get(id=conductores_id)
        ganacia=GanaciasFlete.objects.create(
                turbo=tubro,
                flete = nuevo_flete,
                day = fecha_inicio,
                valor=valor,
                cantidad=Cantidad,
                name= tubro.conductor,
                descripcion=Descripcion


        )
        if ganacia:
            messages.success(request, f"registro con éxito.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")




        return redirect("turbo_register")

class RegisterTravelsGatosView(View):
    template_name = "turbo_registro_gastos.html"

    def __init__(self, **kwargs: Any) -> None:
       ...


    def get(self, request):
         flete=Flete.objects.all()
         turbos=Turbo.objects.all()


         return render(
            request,
            self.template_name,
            {
               "flete":flete,
                "turbos":turbos,
            }

        )

    def post(self, request):
        date_range = request.POST["date_range"].split(" - ")
        valor = request.POST["valor"]
        Cantidad = request.POST["Cantidad"]
        Descripcion = request.POST["Descripcion"]
        conductores_id = request.POST["conductores_ids"]
        flete_ids = request.POST["flete_ids"]
        fecha_inicio_str, fecha_fin_str = date_range

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
        flete=Flete.objects.get(id=flete_ids)
        turbo=Turbo.objects.get(id=conductores_id)

        GastosCarro.objects.create(

            flete = flete,
            turbo=turbo,
            valor=valor,
            cantidad=Cantidad,
            name= turbo.conductor,
            descripcion=Descripcion
        )




        return redirect("turbo_register_gatos")
