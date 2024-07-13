from django.urls import path
from . import views

app_name = "clientes_proveedores"

urlpatterns = [
    path("", views.index, name="index"),
]
