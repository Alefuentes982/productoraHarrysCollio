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
    path("regiones/", views.RegionList.as_view(), name="region_list"),
    path("regiones/<int:pk>/", views.RegionDetail.as_view(), name="region_detail"),
    path("comunas/", views.ComunaList.as_view(), name="comuna_list"),
    path("comunas/<int:pk>/", views.ComunaDetail.as_view(), name="comuna_detail"),
]
