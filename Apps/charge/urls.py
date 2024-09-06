from django.urls import path

from .views import *

urlpatterns = [
    path("turbo_view", TurboView.as_view(), name="turbo_view"),
    path("turbo_register", RegisterTravelsView.as_view(), name="turbo_register"),
    path("turbo_register_gatos", RegisterTravelsGatosView.as_view(), name="turbo_register_gatos"),

]
