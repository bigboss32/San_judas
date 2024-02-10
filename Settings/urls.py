from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.session.urls')),
    path('', include('Apps.base.urls')),
    path('', include('Apps.liter_control.urls')),
    path('', include('Apps.employees.urls')),
    path('', include('Apps.transportation.urls')),
    path('', include('Apps.bills.urls')),

    
 
]
