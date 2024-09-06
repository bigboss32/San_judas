from django.urls import path

from .views import *

urlpatterns = [
    path("Obtener_trasporte", TransportationView.as_view(), name="Obtener_trasporte"),

]
