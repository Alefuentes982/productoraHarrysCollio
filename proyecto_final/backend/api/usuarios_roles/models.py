from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission,
)
from api.ubicacion.models import Region, Comuna


class Rol(models.Model):
    descripcion = models.CharField(max_length=100)
    permisos = models.IntegerField()


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    direccion = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    esta_activo = models.BooleanField(default=True)
    es_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group, related_name="usuarios_roles_user_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name="usuarios_roles_user_set", blank=True
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "nombre",
        "apellido",
        "rut",
        "dv",
        "direccion",
        "region",
        "comuna",
        "telefono",
        "rol",
    ]
