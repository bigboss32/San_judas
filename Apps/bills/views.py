from typing import Any

from django.shortcuts import render
from django.views import View

from Apps.bills.services.obtener_gastos import GetBills


class BillsView(View):
    template_name = "gasto/registar_gasto.html"

    def __init__(self, **kwargs: Any) -> None:
        pass

    def get(self, request):
        return GetBills.obtener_gastos(request, self.template_name)

    def post(self, request):
        pass
