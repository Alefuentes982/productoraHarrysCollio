from rest_framework import generics
from .models import Region, Comuna
from .serializers import RegionSerializer, ComunaSerializer


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ComunaList(generics.ListCreateAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class ComunaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
