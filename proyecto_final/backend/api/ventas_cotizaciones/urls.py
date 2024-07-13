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
    path("ventas/", views.VentasList.as_view(), name="ventas_list"),
    path("ventas/<int:pk>/", views.VentasDetail.as_view(), name="ventas_detail"),
    path("cotizaciones/", views.CotizacionesList.as_view(), name="cotizaciones_list"),
    path(
        "cotizaciones/<int:pk>/",
        views.CotizacionesDetail.as_view(),
        name="cotizaciones_detail",
    ),
]
