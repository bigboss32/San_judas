from django.urls import path

from .views import *

urlpatterns = [
    path("reports", Reports.as_view(), name="reports"),

]
