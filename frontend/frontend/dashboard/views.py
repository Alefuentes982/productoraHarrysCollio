from django.shortcuts import render


def landing(request):
    return render(request, "dashboard/landing.html")


def clientes(request):
    return render(request, "clientes_proveedores/index.html")


def servicios(request):
    return render(request, "servicios_categorias/index.html")


def ventas(request):
    return render(request, "ventas_cotizaciones/index.html")
