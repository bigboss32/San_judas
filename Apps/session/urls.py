from django.urls import path

from .views import *

urlpatterns = [
    path("", InicioSesionView.as_view(), name="Inicio_sesion"),
    path("registro/", RegistarView.as_view(), name="registrar_usuario"),
]
