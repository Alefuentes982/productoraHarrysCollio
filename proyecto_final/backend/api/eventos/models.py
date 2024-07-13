from django.db import models


class Evento(models.Model):
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        "servicios_categorias.Categoria", on_delete=models.CASCADE
    )
    aforo = models.IntegerField()
    cliente = models.ForeignKey(
        "clientes_proveedores.Cliente", on_delete=models.CASCADE
    )
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.ForeignKey(
        "ventas_cotizaciones.EstadoCot", on_delete=models.CASCADE
    )
    comuna = models.ForeignKey("ubicacion.Comuna", on_delete=models.CASCADE)
    servicio = models.ForeignKey(
        "servicios_categorias.Servicio", on_delete=models.CASCADE
    )
