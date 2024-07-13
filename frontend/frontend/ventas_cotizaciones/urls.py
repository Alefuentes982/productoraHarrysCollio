from django.urls import path
from . import views

app_name = "ventas_cotizaciones"

urlpatterns = [
    path("", views.index, name="index"),
]
