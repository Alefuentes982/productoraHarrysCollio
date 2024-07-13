from django.db import models


class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)


class Extra(models.Model):
    descripcion = models.CharField(max_length=100)
    recargo = models.IntegerField()


class Servicio(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    proveedor = models.ForeignKey(
        "clientes_proveedores.Proveedor",
        on_delete=models.CASCADE,
        related_name="servicios_categorias_proveedores",
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE, null=True, blank=True)
