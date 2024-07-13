from rest_framework import serializers
from .models import Usuario, Rol


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = "__all__"
