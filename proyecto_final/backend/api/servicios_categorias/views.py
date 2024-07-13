from rest_framework import generics
from .models import Servicio, Categoria, Extra
from .serializers import ServicioSerializer, CategoriaSerializer, ExtraSerializer


class ServiciosList(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class ServiciosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class CategoriasList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ExtrasList(generics.ListCreateAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class ExtrasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
