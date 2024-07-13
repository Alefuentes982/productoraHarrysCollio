from django.urls import path
from . import views

app_name = "servicios_categorias"

urlpatterns = [
    path("", views.index, name="index"),
]
