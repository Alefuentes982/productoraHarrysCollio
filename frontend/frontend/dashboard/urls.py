from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("clientes/", views.clientes, name="clientes"),
    path("servicios/", views.servicios, name="servicios"),
    path("ventas/", views.ventas, name="ventas"),
]
