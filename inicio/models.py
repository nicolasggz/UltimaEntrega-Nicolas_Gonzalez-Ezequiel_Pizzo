from django.db import models

# Create your models here.

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    propietario = models.ForeignKey('Propietario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
