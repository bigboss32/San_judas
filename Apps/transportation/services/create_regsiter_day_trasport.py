from django.shortcuts import render,redirect
from ...employees.models import Empleado,Rol
from ..models import *
class CreateRegsiterDayTrasport():
        def create_register_day(request):
                valor=request.POST["Valor"]
                trabajo=request.POST["Trabajo"]
                dia=request.POST["Dia"]
                empelado=request.POST["Conductor"]
                automovil=request.POST["Automovil"]
                empelado_data=Empleado.objects.get(id=empelado)
                automovil_data=Automovil.objects.get(id=automovil)    
                breakpoint()            
                if trabajo!='on':
                        trabajo=False
                trabajo=True
                register_day_trasport=RegisterDayTrasport.objects.create(
                        valor=valor,
                        trabajo=trabajo,
                        day = dia
                )
                Trasporte.objects.create(
                        registerdaytrasport=register_day_trasport,
                        empleado= empelado_data,
                        automovil= automovil_data

                )
                return redirect('register_day_trasport')


        def get_day(request,template):
            conductor = Empleado.objects.filter(rol__name="conductor")
            automovil=Automovil.objects.all()
            return render(request, template,{"conductor":conductor,
                                             "automovil":automovil })