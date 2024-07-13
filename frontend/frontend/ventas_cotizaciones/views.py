from django.shortcuts import render


def index(request):
    return render(request, "ventas_cotizaciones/index.html")
