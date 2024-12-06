from django.db import models

class Hospital(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="medicos")

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    enfermedad_diagnosticada = models.TextField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="pacientes")

    def __str__(self):
        return self.nombre
