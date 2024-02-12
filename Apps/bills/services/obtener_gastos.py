from django.shortcuts import render

from .connections.data_base import DataBase


class GetBills:
    def obtener_gastos(request, template_name):
        gastos = DataBase.tipo_de_gatsos()
        return render(request, template_name, {"gastos": gastos})
