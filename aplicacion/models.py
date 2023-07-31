from django.db import models

# Create your models here.

class Paciente(models.Model):

    nombre = models.CharField(max_length=20)

    apellido = models.CharField(max_length=20)
    
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
 

class Consultas(models.Model):

    nombre = models.CharField(max_length=20)

    apellido = models.CharField(max_length=20)
    
    telefono = models.CharField(max_length=20)

    email = models.EmailField()
    
    consulta = models.CharField(max_length=200)


class Turnos(models.Model):

    usuario = models.CharField(max_length=20)

    fecha_Turno = models.DateField()