from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateField(auto_now_add=True)


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateField(auto_now_add=True)


class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)


class Extra(models.Model):
    descripcion = models.CharField(max_length=100)
    recargo = models.IntegerField()


class Servicio(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, related_name="servicios_proveedores"
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE)


class MetodoPago(models.Model):
    descripcion = models.CharField(max_length=100)


class EstadoCot(models.Model):
    descripcion = models.CharField(max_length=100)


class DetalleCotizacion(models.Model):
    vendedor = models.IntegerField()
    evento = models.ForeignKey(
        "eventos.Evento",
        on_delete=models.CASCADE,
        related_name="detallecotizaciones_clientes",
    )
    precio_servicio = models.IntegerField()
    iva = models.IntegerField()
    subtotal = models.IntegerField()


class Cotizacion(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="cotizaciones_clientes"
    )
    detalle_venta = models.ForeignKey(
        DetalleCotizacion,
        on_delete=models.CASCADE,
        related_name="detalle_ventas_clientes",
    )
    estado = models.ForeignKey(EstadoCot, on_delete=models.CASCADE)
    fecha = models.DateField()
    subtotal = models.IntegerField()


class Venta(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="ventas_clientes"
    )
    cotizacion = models.ForeignKey(
        Cotizacion,
        on_delete=models.CASCADE,
        related_name="cotizaciones_ventas_clientes",
    )
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha = models.DateField()
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()


class Reserva(models.Model):
    porcentaje = models.IntegerField()
