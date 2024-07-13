from django.urls import path
from . import views

app_name = "usuarios_roles"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]
