
from django.urls import path
from .views import *

urlpatterns = [
    path('create_automovil', CreateAutomovilView.as_view(), name='create_automovil'),
    path('register_day_trasport', RegisterDayTrasportView.as_view(), name='register_day_trasport'),



]