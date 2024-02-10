

from typing import Any
from django.shortcuts import redirect, render
from .Connections.data_base import Database


class CreateRegister():
    def __init__(self, **kwargs: Any) -> None:
 
        self.database=Database()
    
    def createregisterday(self,request,ruta_id):
    
        auto = request.POST['auto']
        litros = request.POST['litros']
        valor_litro = request.POST['valor_litro']
        avances = request.POST['avances']
        fecha = request.POST['fecha']
        id = request.POST['id']
        total=int(valor_litro)*int(litros)
        total_adelanto=total-int(avances)
        data = {
            'litros': litros,
            'valor_litro': valor_litro,
            'avances': avances,
            'fecha': fecha,
            'id': id ,
            'total':total,
            'total_adelanto':total_adelanto,   
            'ruta_id':ruta_id,   
            "trasporte":auto
        }
        self.database.create_register_day(data)
        return redirect('registro_diario', ruta_id=ruta_id)
    def get_rutas(self,request,ruta_id,template_name):
         provedor=self.database.obtener_provedor(ruta_id)
         trasporte=self.database.obtener_trasporte()
         return render(request,template_name,{"provedor":provedor,"ruta_id":ruta_id,"trasporte":trasporte})