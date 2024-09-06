from django.urls import path

from .views import *

urlpatterns = [
    path("registrar_production", RegisterProductionView.as_view(), name="registrar_production"),

]
