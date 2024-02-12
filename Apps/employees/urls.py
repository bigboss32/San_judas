from django.urls import path

from .views import *

urlpatterns = [
    path("new_employees", EmployeesView.as_view(), name="new_employees"),
    path("new_rol", CreateRolEmployeesView.as_view(), name="new_rol"),
    path(
        "register_day_employ",
        RegisterDayEmployView.as_view(),
        name="register_day_employ",
    ),
]
