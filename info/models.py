from django.db import models

class Informacion(models.Model):

    actualizacion = models.TextField(null=True, max_length=800)
    fecha = models.DateField(null=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        verbose_name_plural = "informacion"
        get_latest_by = 'fecha'

class Usuarios(models.Model):

    nombre = models.CharField(max_length=30, null=True)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre +' '+ self.apellido

    class Meta:
        verbose_name_plural = "usuarios"

class Front(models.Model):

    titulo = models.CharField(max_length=30, null=True)
    informacion_adicional = models.TextField(null=True, max_length=3000)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "front"
