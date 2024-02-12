from django.contrib import messages
from django.shortcuts import redirect, render

from Apps.employees.models import Empleado, Rol


class CreateEmploy:
    def create_empleado(request):

        rol = request.POST["rol"]
        rols = Rol.objects.get(id=rol)
        first_name = request.POST["primernombre"]
        second_name = request.POST["segundonombre"]
        last_name = request.POST["primerapellido"]
        second_last_name = request.POST["segundoapellido"]
        cedula = request.POST["cedula"]
        Empleado.objects.create(
            rol=rols,
            first_name=first_name,
            second_name=second_name,
            last_name=last_name,
            second_last_name=second_last_name,
            cedula=cedula,
            estado=True,
        )

        messages.success(request, f"registro con éxito.")

        return redirect("new_employees")

    def obtener_rol(request, template_name):
        rol = Rol.objects.all()
        return render(request, template_name, {"rol": rol})
