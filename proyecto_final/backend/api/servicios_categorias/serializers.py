from rest_framework import serializers
from .models import Servicio, Categoria, Extra


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = "__all__"
