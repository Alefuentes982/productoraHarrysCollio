from rest_framework import generics
from .models import Venta, Cotizacion
from .serializers import VentaSerializer, CotizacionSerializer


class VentasList(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


class VentasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


class CotizacionesList(generics.ListCreateAPIView):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer


class CotizacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer
