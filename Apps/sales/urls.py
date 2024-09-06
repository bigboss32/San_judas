from django.urls import path

from .views import *

urlpatterns = [
    path("registrar_ventas", RegisterSalesView.as_view(), name="registrar_ventas"),

]
