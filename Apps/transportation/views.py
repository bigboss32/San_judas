from django.views import View

from .services.create_automovil import CreateAutomovil
from .services.create_regsiter_day_trasport import CreateRegsiterDayTrasport


class CreateAutomovilView(View):
    template_name = "automovil/registar_autos.html"

    def get(self, request):
        return CreateAutomovil.get_automovil(request, self.template_name)

    def post(self, request):
        return CreateAutomovil.create_automovil(request)


class RegisterDayTrasportView(View):
    template_name = "registtar_diario/registar_diario.html"

    def get(self, request):
        return CreateRegsiterDayTrasport.get_day(request, self.template_name)

    def post(self, request):
        return CreateRegsiterDayTrasport.create_register_day(request)
