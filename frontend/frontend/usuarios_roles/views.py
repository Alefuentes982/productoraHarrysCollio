from django.shortcuts import render


def register(request):
    return render(request, "usuarios_roles/register.html")


def login(request):
    return render(request, "usuarios_roles/login.html")
