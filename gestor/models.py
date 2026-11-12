from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='proyectos'
    )
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
  '''
  Modelo que representa una tarea de un proyecto
  '''

  PRIORIDAD_CHOICES = [
    ('BAJA', 'Baja'),
    ('MEDIA', 'Media'),
    ('ALTA', 'Alta'),
  ]

  ESTADO_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('EN_PROGRESO', 'En progreso'),
    ('COMPLETADA', 'Completada'),
  ]

  proyecto = models.ForeignKey(
    Proyecto,
    on_delete=models.CASCADE,
    related_name="tareas"
  )
  titulo = models.CharField(max_length=100)
  descripcion = models.TextField()
  prioridad = models.CharField(
    max_length=5,
    choices=PRIORIDAD_CHOICES,
    default='MEDIA'
  )
  estado = models.CharField(
    max_length=11,
    choices=ESTADO_CHOICES,
    default='PENDIENTE'
  )