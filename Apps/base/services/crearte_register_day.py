from typing import Any

from django.shortcuts import redirect, render

from .Connections.data_base import Database


class CreateRegister:
    def __init__(self, **kwargs: Any) -> None:

        self.database = Database()

    def createregisterday(self, request, ruta_id):


        litros = request.POST["litros"]
        valor_litro = request.POST["valor_litro"]
        avances = request.POST["avances"]
        fecha = request.POST["fecha"]
        id = request.POST["id"]
        id_trasporte = request.POST["id_trasporte"]
        Valor_tras = request.POST["Valor_tras"]
        Litros_eli = request.POST["Litros_eli"]

        data = {
            "litros": litros,
            "valor_litro": valor_litro,
            "avances": avances,
            "fecha": fecha,
            "id": id,
            "ruta_id": ruta_id,
            "id_trasporte":id_trasporte,
            "Valor_tras":Valor_tras,
            "Litros_eli":Litros_eli,

        }

        registerday=self.database.create_register_day(data)
        self.database.create_register_day_trasport(data,registerday)
        url_completa = f"/registro_diario/{ruta_id}/?fecha={fecha}"
        return redirect(url_completa)


    def get_rutas(self, request, ruta_id, template_name):
        provedor = self.database.obtener_provedor(ruta_id,request)
        trasporte = self.database.obtener_trasporte(ruta_id)
        fecha=request.GET.get('fecha')
        return render(
            request,
            template_name,
            {"provedor": provedor, "ruta_id": ruta_id, "trasporte": trasporte,"fecha_seleccionada":fecha},
        )
