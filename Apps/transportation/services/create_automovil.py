from django.shortcuts import render,redirect
from ..models import Automovil
from django.contrib import messages

class CreateAutomovil():
    def create_automovil(request):
        estado=request.POST["estado"]
        color=request.POST["color"]
        placa=request.POST["placa"]
        tipo=request.POST["tipo"]

        Automovil.objects.create(
            tipo=tipo,
            placa=placa,
            color=color,
            estado=estado

        )
        messages.success(request, f"registro con éxito.")
        return redirect("create_automovil")


    def get_automovil(request,template):
        return render(request, template)