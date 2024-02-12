from django.shortcuts import redirect

from Apps.employees.models import Rol


class Rolcreate:
    @staticmethod
    def create_rol_employ(request):
        name_post = request.POST["rol_empelado"]
        Rol.objects.create(name=name_post)
        return redirect("new_employees")
