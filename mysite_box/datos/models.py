from django.db import models

class DatosUsuario(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.IntegerField()

    class Meta:
        app_label = 'datos'
        verbose_name = 'Usuarios'
    
    def __str__(self):
        return (f'{self.nombre} {self.apellido}')

class Profesionales(models.Model):
    profesion = models.CharField(max_length=250)
    anio_egreso = models.DateTimeField()
    experiencia = models.IntegerField()
    experiencia_docente = models.IntegerField()

    class Meta:
        verbose_name = 'Profesionales'