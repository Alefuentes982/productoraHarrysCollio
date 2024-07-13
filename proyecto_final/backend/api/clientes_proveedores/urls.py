"""
URL configuration for hc_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.ClientesList.as_view(), name="clientes_list"),
    path("clientes/<int:pk>/", views.ClientesDetail.as_view(), name="clientes_detail"),
    path("proveedores/", views.ProveedoresList.as_view(), name="proveedores_list"),
    path(
        "proveedores/<int:pk>/",
        views.ProveedoresDetail.as_view(),
        name="proveedores_detail",
    ),
]
