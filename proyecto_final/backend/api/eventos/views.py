from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer


class EventosList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class EventosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
