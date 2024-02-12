from django.shortcuts import render
from django.views import View

from .services.crear_empelados import CreateEmploy
from .services.crear_rol_empelados import Rolcreate


class EmployeesView(View):
    template_name = "empleados/registar_empleados.html"

    def get(self, request):
        return CreateEmploy.obtener_rol(request, self.template_name)

    def post(self, request):
        return CreateEmploy.create_empleado(request)


class CreateRolEmployeesView(View):
    template_name = "empleados/registar_empleados.html"

    def post(self, request):
        return Rolcreate.create_rol_employ(request)


class RegisterDayEmployView(View):
    template_name = "empleados/registar_empleados.html"

    def get(self, request):
        return CreateEmploy.obtener_rol(request, self.template_name)

    def post(self, request):
        return CreateEmploy.create_empleado(request)
