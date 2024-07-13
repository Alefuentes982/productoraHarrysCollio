from rest_framework import serializers
from .models import Venta, Cotizacion


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = "__all__"


class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = "__all__"
