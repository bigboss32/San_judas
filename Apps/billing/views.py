from collections import defaultdict
from django.http import HttpResponse
from .models import DeudaProveedor
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from datetime import datetime, timedelta
from Apps.liter_control.models import RegisterDay,Provedor
from Apps.transportation.models import RegisterDayTrasporte
from .services.generar_pdf import GeneratePdf
from django.utils.timezone import make_aware

class CreateBilling(View):
    template_name = "billing/generation_billing.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        date_range = request.POST["range"].split(" - ")
        fecha_inicio_str, fecha_fin_str = date_range

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
        cantidad_dias = (fecha_fin - fecha_inicio).days
        print(cantidad_dias)
        print(fecha_fin)
        print(fecha_inicio)
        trasporte = []

        registros = RegisterDay.objects.filter(day__range=(fecha_inicio, fecha_fin))
        proveedores = []
        for registro in registros:
            litros_por_dia = [0] * int(cantidad_dias+1)
            adelantos=0
            total_litros = 0

            for otro_registro in registros:
                dia_index = (otro_registro.day.day - fecha_inicio.day)
                if registro.provedor.first_name == otro_registro.provedor.first_name:
                    deuda=DeudaProveedor.objects.filter(provedor=otro_registro.provedor)
                    if not deuda:
                        # Crear una nueva deuda para el proveedor
                        nueva_deuda = DeudaProveedor(provedor=otro_registro.provedor, valor_total_deuda=0)  # Ajusta esto según tu modelo
                        nueva_deuda.save()
                    total_litros += otro_registro.liter
                    litros_por_dia[dia_index] += otro_registro.liter
                    total_a_pagar=total_litros*otro_registro.value_liter
                    adelantos+=otro_registro.adelantos
                    valor_total_pagar=total_a_pagar-(adelantos+deuda.first().valor_total_deuda)

            trasporte_existente = next((p for p in proveedores if p["nombre"] == registro.provedor.first_name), None)
            if trasporte_existente:
                ...
            else:
                nuevo_proveedor = {
                "id":registro.provedor.id,
                "nombre": registro.provedor.first_name,
                "ruta": registro.provedor.ruta,
                "factura": 1,
                "litros": total_litros,
                "fecha": fecha_inicio_str,
                "dia": list(range(1, cantidad_dias + 2)),
                "dia_leche": litros_por_dia,
                "fecha_final": fecha_fin_str,
                "adelantos": adelantos,
                "valor_litro": registro.value_liter,
                "Total_pagar": total_a_pagar,
                "valor_total_pagar": valor_total_pagar,
                "deuda":deuda.first().valor_total_deuda

                }
                if valor_total_pagar<0:
                        deuda_pimera=deuda.first()
                        deuda_pimera.valor_total_deuda=abs(valor_total_pagar)
                        deuda_pimera.save()
                else:
                    deuda_pimera=deuda.first()
                    deuda_pimera.valor_total_deuda=0
                    deuda_pimera.save()
                if total_litros!=0:
                 proveedores.append(nuevo_proveedor)



        instancai= GeneratePdf()
        return instancai.open_pdf(proveedores)

class CreateBillingTrasportation(View):
    template_name = "billing/generation_billing.html"

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):

        date_range = request.POST["range_trasport"].split(" - ")
        fecha_inicio_str, fecha_fin_str = date_range
        total_litors_dias = {}

        fecha_inicio = datetime.strptime(fecha_inicio_str, "%m/%d/%Y")
        fecha_fin = datetime.strptime(fecha_fin_str, "%m/%d/%Y")
        cantidad_dias = (fecha_fin - fecha_inicio).days

        registros = RegisterDayTrasporte.objects.filter(registerday__day__range=(fecha_inicio, fecha_fin))
        trasporte = []
        dias_leche = list(range(1, 16))
        for registro in registros:
            litros_por_dia = [0] * int(cantidad_dias+1)
            total_litros_transportados = 0
            adelantos=0
            total_litros_perdidos=0
            conductor = registro.trasporte.conductor
            dia = registro.registerday.day.day  # Obtenemos solo el día de la fecha

            # Sumamos los litros transportados para este registro al total para este día y conductor
        # Imprimimos los resultados
            from datetime import timedelta
            # Iteramos sobre todos los registros para encontrar los litros transportados por este conductor
            for otro_registro in registros:
                if registro.trasporte.conductor == otro_registro.trasporte.conductor:

                    total_litros_transportados += otro_registro.registerday.liter
                    total_litros_perdidos += otro_registro.litros_no_llegaron
                    diferencia_dias  = (otro_registro.registerday.day - fecha_inicio.date()).days
                    dia_index = diferencia_dias if diferencia_dias >= 0 else 0
                    print(otro_registro.registerday.day.day)
                    print(fecha_inicio.day)

                # Sumar los litros transportados de este registro al día correspondiente
                    litros_por_dia[dia_index] += otro_registro.registerday.liter
                    adelantos += otro_registro.adelantos
            trasporte_existente = next((p for p in trasporte if p["nombre"] == registro.trasporte.conductor), None)
            if trasporte_existente:
                dia_index = registro.registerday.day.day - fecha_inicio.day  # Obtenemos el índice del día en el arreglo

            else:
                dia_leche = [0] * 15  # Inicializamos el arreglo con ceros
                dia_index = registro.registerday.day.day - fecha_inicio.day  # Obtenemos el índice del día en el arreglo
                dia_leche[dia_index] = registro.registerday.liter

                valores_por_litro_conductor = []
                valores_por_litro_conductor_provedores = []
                valorpordia=[]

                # Iteramos sobre todos los registros para calcular el promedio del valor por litro para este conductor
                for otro_registro in registros:
                    if registro.trasporte.conductor == otro_registro.trasporte.conductor:
                        valores_por_litro_conductor.append(otro_registro.value_liter_traspo)
                        valores_por_litro_conductor_provedores.append(otro_registro.registerday.value_liter)


                # Calculamos el promedio para el conductor actual
                if valores_por_litro_conductor:
                    promedio_value_liter_traspo_conductor = sum(valores_por_litro_conductor) / len(valores_por_litro_conductor)
                    promedio_value_liter_day = sum(valores_por_litro_conductor_provedores) / len(valores_por_litro_conductor_provedores)
                else:
                    promedio_value_liter_traspo_conductor = 0  # Si no hay valores, el promedio es 0

                total_a_pagar = (total_litros_transportados * promedio_value_liter_traspo_conductor)-(total_litros_perdidos*(promedio_value_liter_day+promedio_value_liter_traspo_conductor))


                total_a_pagar_menos_adelantos=total_a_pagar-adelantos
                nuevo_proveedor = {
                "id":registro.trasporte.id,
                "nombre": registro.trasporte.conductor,
                "ruta": registro.trasporte.ruta,
                "factura": 1,
                "Valor por litro":promedio_value_liter_traspo_conductor,
                "Total de litros trasportados":total_litros_transportados,
                "litros que no llegaron":total_litros_perdidos,
                "Valor litro provedor":promedio_value_liter_day+promedio_value_liter_traspo_conductor,
                "total ha pagar":total_a_pagar_menos_adelantos,
                "adelantos":adelantos,
                "total a pagar sin adelantos":total_a_pagar,
                "fecha final": fecha_fin_str,
                "fecha incio":fecha_inicio_str,
                "litros_por_dia": litros_por_dia,



                }

                trasporte.append(nuevo_proveedor)


        instancai= GeneratePdf()
        return instancai.open_pdf_trasporte(trasporte)
