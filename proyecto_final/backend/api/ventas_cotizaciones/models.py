from django.db import models


class MetodoPago(models.Model):
    descripcion = models.CharField(max_length=100)


class EstadoCot(models.Model):
    descripcion = models.CharField(max_length=100)


class DetalleCotizacion(models.Model):
    vendedor = models.IntegerField()
    evento = models.ForeignKey(
        "eventos.Evento",
        on_delete=models.CASCADE,
        related_name="detallecotizaciones_ventas",
    )
    precio_servicio = models.IntegerField()
    iva = models.IntegerField()
    subtotal = models.IntegerField()


class Cotizacion(models.Model):
    cliente = models.ForeignKey(
        "clientes_proveedores.Cliente",
        on_delete=models.CASCADE,
        related_name="cotizaciones_ventas",
    )
    detalle_venta = models.ForeignKey(
        DetalleCotizacion,
        on_delete=models.CASCADE,
        related_name="detalle_ventas_ventas",
    )
    estado = models.ForeignKey(EstadoCot, on_delete=models.CASCADE)
    fecha = models.DateField()
    subtotal = models.IntegerField()


class Venta(models.Model):
    cliente = models.ForeignKey(
        "clientes_proveedores.Cliente",
        on_delete=models.CASCADE,
        related_name="ventas_ventas",
    )
    cotizacion = models.ForeignKey(
        Cotizacion, on_delete=models.CASCADE, related_name="cotizaciones_ventas_ventas"
    )
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha = models.DateField()
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()


class Reserva(models.Model):
    porcentaje = models.IntegerField()
