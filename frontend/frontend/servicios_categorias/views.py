from django.shortcuts import render


def index(request):
    return render(request, "servicios_categorias/index.html")
