from django.urls import path

from .views import *

urlpatterns = [
    path("registrar_gastos", BillsView.as_view(), name="registrar_gastos"),
]
