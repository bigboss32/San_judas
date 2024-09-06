
from datetime import datetime, timedelta
from django.shortcuts import render
from django.views import View
from Apps.liter_control.models import Provedor, RegisterDay, Ruta
from Apps.sales.models import Ventas
from Apps.production.models import ProductionProducto
from Apps.transportation.models import RegisterDayTrasporte

from django.utils import timezone
from Apps.bills.models import Gastos
from django.db.models.functions import ExtractDay
from django.db.models import Sum, F

class Indexview(View):
    template_name = "main.html"

    def get(self, request):

        total_provedores = Provedor.objects.count()
        total_ruta = Ruta.objects.count()


        fecha_actual = datetime.now()

        primer_dia_mes = fecha_actual.replace(day=1)
        primer_dia_proximo_mes = (primer_dia_mes + timedelta(days=32)).replace(day=1)
        duracion_mes = (primer_dia_proximo_mes - primer_dia_mes).days
        nombres_dias_mes = [primer_dia_mes.strftime('%B %d')]

        for i in range(1, duracion_mes):
            nombres_dias_mes.append((primer_dia_mes + timedelta(days=i)).strftime('%B %d'))

        mes_actual = timezone.now().month


        suma_total_por_dia_mes_actual = (
            RegisterDay.objects.filter(day__month=mes_actual)
            .annotate(dia_del_mes=ExtractDay("day"))  # Cambiado el alias a "dia_del_mes"
            .values("dia_del_mes")
            .annotate(suma_total=Sum(F("value_liter") * F("liter")))
            .order_by("dia_del_mes")
        )
        total_total_en_toda_la_consulta = suma_total_por_dia_mes_actual.aggregate(
            total_total_en_toda_la_consulta=Sum("suma_total")
        )["total_total_en_toda_la_consulta"]




        # Filtrar los registros de RegisterDay para el mes actual
        registros_mes_actual = RegisterDay.objects.filter(day__month=mes_actual)
        # Obtener la suma de litros por ruta para el mes actual
        litros_por_ruta_mes_actual = registros_mes_actual.values('ruta__name_route',).annotate(total_litros=Sum('liter'))
        suma_total_litros_mes_actual = registros_mes_actual.aggregate(total_litros_total=Sum('liter'))['total_litros_total']
        adelantos_totales_mes_actual = registros_mes_actual.aggregate(total_adelantos=Sum('adelantos'))['total_adelantos']
        gasto_total_mes_actual = Gastos.objects.filter(day__month=mes_actual).aggregate(
    gasto_total=Sum(F('valor') * F('cantidad'))
)['gasto_total']
        print(gasto_total_mes_actual)
       # Obtener la cantidad de leche por día de producción

        cantidad_leche_por_dia = RegisterDay.objects.filter(day__month=mes_actual) \
                                            .values('day') \
                                            .annotate(total_liter=Sum('liter')) \
                                            .order_by('day')

        cantidad_producto_por_mes = ProductionProducto.objects.filter(producionday__day__month=mes_actual) \
                                                      .values('producionday__day') \
                                                      .annotate(total_cantidad_producto=Sum('cantidad')) \
                                                      .order_by('producionday__day')
        # cantidad_por_dia contiene la cantidad total de litros de leche por día de producción
        for item in cantidad_leche_por_dia:
            print(f"Día de producción: {item['day']}, Cantidad de leche: {item['total_liter']}")

        resultados = []
        for registro_leche in cantidad_leche_por_dia:
            registro_producto = next((item for item in cantidad_producto_por_mes if item['producionday__day'] == registro_leche['day']), None)
            if registro_producto:
                promedio = registro_leche['total_liter'] / registro_producto['total_cantidad_producto']
            else:
                promedio = 0  # Establecer un valor predeterminado de 0 si no hay datos para ese día
            resultados.append({'fecha': registro_leche['day'], 'promedio': promedio})


        hoy = datetime.now()


# Supongamos que Ventas es el nombre de tu modelo

        resultado = Ventas.objects.filter(fecha_venta_incio__month=mes_actual) \
                                .annotate(total_venta=F('cantidad') * F('valor')) \
                                .aggregate(total_cantidad=Sum('total_venta'), total_ventas=Sum('cantidad'))
        print(resultado)
        resultados_por_conductor = RegisterDayTrasporte.objects.filter(
        registerday__day__month=mes_actual # Filtrar por rango de fechas
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
        total_litros_valen_total = resultados_por_conductor.aggregate(total_litros_valen_total=Sum('total_a_pagar_menosleche_perdida'))
        nombres_meses = [
            'Enero', 'Febrero', 'Marzo', 'Abril',
            'Mayo', 'Junio', 'Julio', 'Agosto',
            'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]

        # Obtener el año actual
        anio_actual = timezone.now().year

        # Crear una lista de objetos para cada mes con su año correspondiente
        meses_con_anio = []
        contador=1

        for nombre_mes in nombres_meses:


            if contador==timezone.now().month:
                estatus="active"
            else:
                estatus=""

            mes = {
                'mes':contador,
                'nombre': nombre_mes,
                'anio': anio_actual,
                'estatus':estatus
            }
            contador+=1
            meses_con_anio.append(mes)


        return render(
            request,
            self.template_name,
            {
                'labels': nombres_dias_mes,
                "total_provedores": total_provedores,
                "total_ruta": total_ruta,
                "total_automoviles": 2,
                "total_total_en_toda_la_consulta":total_total_en_toda_la_consulta,
                "litros_por_mes":suma_total_por_dia_mes_actual,
                "litros_por_ruta":litros_por_ruta_mes_actual,
                "leche_total_rutas":suma_total_litros_mes_actual,
                "value_total_adelantos":gasto_total_mes_actual,
                "resultados":resultados,
                "resultado_ventas":resultado,
                "total_litros_valen_total":total_litros_valen_total,
                "meses_con_anio":meses_con_anio
            },
        )

    def post(self, request): ...
class IndexDateView(View):
     template_name = "main.html"
     def post(self, request): ...

     def get(self, request,mes,year):
            total_provedores = Provedor.objects.count()
            total_ruta = Ruta.objects.count()


            fecha_actual = datetime.now()
            fecha_actual = fecha_actual.replace(month=mes)
            primer_dia_mes = fecha_actual.replace(day=1)
            primer_dia_proximo_mes = (primer_dia_mes + timedelta(days=32)).replace(day=1)
            duracion_mes = (primer_dia_proximo_mes - primer_dia_mes).days
            nombres_dias_mes = [primer_dia_mes.strftime('%B %d')]

            for i in range(1, duracion_mes):
                nombres_dias_mes.append((primer_dia_mes + timedelta(days=i)).strftime('%B %d'))



            suma_total_por_dia_mes_actual = (
                RegisterDay.objects.filter(day__month=mes,day__year=year)
                .annotate(dia_del_mes=ExtractDay("day"))  # Cambiado el alias a "dia_del_mes"
                .values("dia_del_mes")
                .annotate(suma_total=Sum(F("value_liter") * F("liter")))
                .order_by("dia_del_mes")
            )
            total_total_en_toda_la_consulta = suma_total_por_dia_mes_actual.aggregate(
                total_total_en_toda_la_consulta=Sum("suma_total")
            )["total_total_en_toda_la_consulta"]

            suma_total_por_dia_mes_pasado = (
                RegisterDay.objects.filter(day__month=mes-1,day__year=year)
                .annotate(dia_del_mes=ExtractDay("day"))  # Cambiado el alias a "dia_del_mes"
                .values("dia_del_mes")
                .annotate(suma_total=Sum(F("value_liter") * F("liter")))
                .order_by("dia_del_mes")
            )
            total_total_en_toda_la_consulta_mes_pasado = suma_total_por_dia_mes_pasado.aggregate(
                total_total_en_toda_la_consulta=Sum("suma_total")
            )["total_total_en_toda_la_consulta"]



            # Filtrar los registros de RegisterDay para el mes actual
            registros_mes_actual = RegisterDay.objects.filter(day__month=mes,data_register__year=year)

            # Obtener la suma de litros por ruta para el mes actual
            litros_por_ruta_mes_actual = registros_mes_actual.values('ruta__name_route',).annotate(total_litros=Sum('liter'))
            suma_total_litros_mes_actual = registros_mes_actual.aggregate(total_litros_total=Sum('liter'))['total_litros_total']
            adelantos_totales_mes_actual = registros_mes_actual.aggregate(total_adelantos=Sum('adelantos'))['total_adelantos']
            gasto_total_mes_actual = Gastos.objects.filter(day__month=mes).aggregate(
            gasto_total=Sum(F('valor') * F('cantidad'))
)['gasto_total']
            print(gasto_total_mes_actual)


        # Obtener la cantidad de leche por día de producción
            cantidad_leche_por_dia = RegisterDay.objects.filter(day__month=mes,day__year=year) \
                                            .values('day') \
                                            .annotate(total_liter=Sum('liter')) \
                                            .order_by('day')

            cantidad_producto_por_mes = ProductionProducto.objects.filter(producionday__day__month=mes,producionday__day__year=year) \
                                                      .values('producionday__day') \
                                                      .annotate(total_cantidad_producto=Sum('cantidad')) \
                                                      .order_by('producionday__day')
            # cantidad_por_dia contiene la cantidad total de litros de leche por día de producción

            resultados = []
            for registro_leche in cantidad_leche_por_dia:
                registro_producto = next((item for item in cantidad_producto_por_mes if item['producionday__day'] == registro_leche['day']), None)
                if registro_producto:
                    promedio = registro_leche['total_liter'] / registro_producto['total_cantidad_producto']
                else:
                    promedio = 0  # Establecer un valor predeterminado de 0 si no hay datos para ese día
                resultados.append({'fecha': registro_leche['day'], 'promedio': promedio})



    # Supongamos que Ventas es el nombre de tu modelo

            resultado = Ventas.objects.filter(fecha_venta_incio__month=mes,fecha_venta_incio__year=year) \
                                    .annotate(total_venta=F('cantidad') * F('valor')) \
                                    .aggregate(total_cantidad=Sum('total_venta'), total_ventas=Sum('cantidad'))
            print(resultado)
            resultados_por_conductor = RegisterDayTrasporte.objects.filter(
            registerday__day__month=mes,
              registerday__day__year=year # Filtrar por rango de fechas
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
            total_litros_trasporte_valor = resultados_por_conductor.aggregate(total_litros_valen_total=Sum('total_a_pagar_menosleche_perdida'))
            nombres_meses = [
                'Enero', 'Febrero', 'Marzo', 'Abril',
                'Mayo', 'Junio', 'Julio', 'Agosto',
                'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
            ]

            # Obtener el año actual
            anio_actual = timezone.now().year

            # Crear una lista de objetos para cada mes con su año correspondiente
            meses_con_anio = []
            contador=1

            for nombre_mes in nombres_meses:

                if contador==mes:
                    estatus="active"
                else:
                    estatus="false"

                meses = {
                    'mes':contador,
                    'nombre': nombre_mes,
                    'anio': anio_actual,
                    'estatus':estatus
                }
                contador+=1
                meses_con_anio.append(meses)

            if total_total_en_toda_la_consulta is None:
                total_total_en_toda_la_consulta = 0

            if gasto_total_mes_actual is None:
                gasto_total_mes_actual = 0

            if total_litros_trasporte_valor is None:
                total_litros_trasporte_valor = {"total_litros_valen_total": 0}

            if resultado is None:
                resultado = {"total_cantidad": 0}
            else:
                if resultado.get("total_cantidad") is None:
                    resultado["total_cantidad"] = 0

            rentabilidad=resultado["total_cantidad"]-(total_total_en_toda_la_consulta+gasto_total_mes_actual+total_litros_trasporte_valor["total_litros_valen_total"])
            print(rentabilidad)
            print(resultado)

            return render(
                request,
                self.template_name,
                {
                    'labels': nombres_dias_mes,
                    "total_provedores": total_provedores,
                    "total_ruta": total_ruta,
                    "total_automoviles": 2,
                    "total_total_en_toda_la_consulta":total_total_en_toda_la_consulta,
                    "litros_por_mes":suma_total_por_dia_mes_actual,
                    "litros_por_ruta":litros_por_ruta_mes_actual,
                    "leche_total_rutas":suma_total_litros_mes_actual,
                    "gasto_total_mes_actual":gasto_total_mes_actual,
                    "resultados":resultados,
                    "resultado_ventas":resultado,
                    "total_litros_trasporte_valor":total_litros_trasporte_valor,
                    "meses_con_anio":meses_con_anio,
                    "rentabilidad":rentabilidad
                },
            )
