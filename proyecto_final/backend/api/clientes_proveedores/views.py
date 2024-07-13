from rest_framework import generics
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
from .serializers import (
    ClienteSerializer,
    ProveedorSerializer,
    CategoriaSerializer,
    ExtraSerializer,
    ServicioSerializer,
    MetodoPagoSerializer,
    EstadoCotSerializer,
    DetalleCotizacionSerializer,
    CotizacionSerializer,
    VentaSerializer,
    ReservaSerializer,
)


class ClientesList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProveedoresList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProveedoresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
