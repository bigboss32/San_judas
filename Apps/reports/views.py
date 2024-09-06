from collections import defaultdict
from django.http import HttpResponse

from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from datetime import datetime, timedelta
from Apps.liter_control.models import RegisterDay,Provedor
from Apps.transportation.models import RegisterDayTrasporte
from django.db.models import F, Sum
from datetime import datetime
from django.utils.timezone import make_aware


class Reports(View):
    template_name = "reports/reports.html"

    def get(self, request):
        fecha_inicio = datetime(year=2024, month=3, day=1)
        fecha_fin = datetime(year=2024, month=3, day=10)  # Suponiendo que sea el 10 de marzo de 2024 como fecha final

        # Obtener el valor total de la tabla RegisterDay para el rango de fechas
        valor_total_tabla_rango_fechas = RegisterDay.objects.filter(day__range=(fecha_inicio, fecha_fin)).aggregate(total=Sum(F('liter') * F('value_liter')))

        # Acceder al valor total
        total_valor_tabla_rango_fechas = valor_total_tabla_rango_fechas['total']

        print("Valor total de la tabla RegisterDay para el rango de fechas:", total_valor_tabla_rango_fechas)
        return render(request, self.template_name)
