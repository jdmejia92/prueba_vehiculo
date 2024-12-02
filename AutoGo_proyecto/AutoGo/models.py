from django.db import models

class Usuario(models.Model):
    DNI = models.IntegerField()
    Tier = models.IntegerField(choices=[(0, 'Básico'), (1, 'Intermedio'), (2, 'Avanzado')])
    Nombres = models.CharField(max_length=255)
    Correo = models.EmailField(unique=True)
    Contraseña = models.CharField(max_length=255)

class Vehiculo(models.Model):
    Placa = models.CharField(max_length=20, unique=True)
    Modelo = models.CharField(max_length=255)
    Marca = models.CharField(max_length=255)
    Año = models.IntegerField()
    CantidadAsientos = models.IntegerField()
    Tipo = models.CharField(max_length=255)
    EstadoReserva = models.CharField(max_length=50, choices=[
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('en_demora', 'En Demora'),
        ('falta', 'Falta'),
    ])

class Reserva(models.Model):
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    EstadoReserva = models.BooleanField()
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    IdVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

class Pago(models.Model):
    Fecha = models.DateField()
    Monto = models.FloatField()
    MetodoDePago = models.CharField(max_length=255)
    Banco = models.CharField(max_length=255, blank=True, null=True)
    IdReserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

class Precio(models.Model):
    PrecioDia = models.FloatField()
    PrecioSemana = models.FloatField()
    PrecioMes = models.FloatField()
    IdVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

