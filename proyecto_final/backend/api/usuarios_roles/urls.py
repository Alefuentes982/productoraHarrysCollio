from django.urls import path
from . import views

urlpatterns = [
    path("", views.UsuariosRolesList.as_view(), name="usuarios_roles_list"),
    path(
        "<int:pk>/", views.UsuariosRolesDetail.as_view(), name="usuarios_roles_detail"
    ),
    path("roles/", views.RolesList.as_view(), name="roles_list"),
    path("roles/<int:pk>/", views.RolesDetail.as_view(), name="roles_detail"),
]
