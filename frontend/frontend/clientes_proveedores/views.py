from django.shortcuts import render


def index(request):
    return render(request, "clientes_proveedores/index.html")
