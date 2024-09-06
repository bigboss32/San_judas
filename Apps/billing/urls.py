from django.urls import path

from .views import *

urlpatterns = [
    path("create_billing", CreateBilling.as_view(), name="create_billing"),
    path("create_billing_trasportation", CreateBillingTrasportation.as_view(), name="create_billing_trasportation"),
]
