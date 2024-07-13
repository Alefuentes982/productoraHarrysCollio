from rest_framework import serializers
from .models import (
    Cliente,
    Proveedor,
    Categoria,
    Extra,
    Servicio,
    MetodoPago,
    EstadoCot,
    DetalleCotizacion,
    Cotizacion,
    Venta,
    Reserva,
)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = "__all__"


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = "__all__"


class EstadoCotSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCot
        fields = "__all__"


class DetalleCotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCotizacion
        fields = "__all__"


class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = "__all__"


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = "__all__"


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"
