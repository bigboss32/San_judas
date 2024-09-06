from django.urls import path

from .views import *

urlpatterns = [
    path("index", Indexview.as_view(), name="index"),
    path("indexdateview/<int:mes>/<int:year>/", IndexDateView.as_view(), name="indexdateview"),
]
