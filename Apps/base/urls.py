from django.urls import path

from .views import *

urlpatterns = [
    path("index", Indexview.as_view(), name="index"),
]
