from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Apps.session.urls")),
    path("", include("Apps.base.urls")),
    path("", include("Apps.liter_control.urls")),
    path("", include("Apps.employees.urls")),
    path("", include("Apps.transportation.urls")),

    path("", include("Apps.bills.urls")),
    path("", include("Apps.billing.urls")),
    path("", include("Apps.sales.urls")),
    path("", include("Apps.production.urls")),
    path("", include("Apps.reports.urls")),
    path("", include("Apps.charge.urls")),
   # path("", include("Apps.transportation.urls")),
]
