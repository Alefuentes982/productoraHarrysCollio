from rest_framework import generics
from .models import Usuario, Rol
from .serializers import UsuarioSerializer, RolSerializer


class UsuariosRolesList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuariosRolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class RolesList(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class RolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
