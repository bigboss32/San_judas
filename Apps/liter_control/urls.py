from django.urls import path

from .views import *

urlpatterns = [
    path("crear_provedores", CrearProvedoresView.as_view(), name="crearprovedores"),
    path("crear_rutas", CrearRutasView.as_view(), name="crear_rutas"),
    path(
        "registro_diario/<int:ruta_id>/", LiterDayView.as_view(), name="registro_diario"
    ),
    path("seleccionar_rutas", SelectRutaView.as_view(), name="seleccionar_rutas"),
    path("obtener_provedores", ObtenerProvedores.as_view(), name="obtener_provedores"),
]
