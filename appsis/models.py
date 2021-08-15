from django.db import models

# Create your models here.



class Persona(models.Model):

    rut = models.CharField(max_length=10, verbose_name = "Rut")
    nombre = models.CharField(max_length=150, verbose_name = "Nombre")
    apellido = models.CharField(max_length=150, verbose_name = "Apellido")
    estado = models.BooleanField(verbose_name = "Estado")
    image = models.ImageField(default='null', verbose_name = "Imagen", upload_to='persona')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Editado")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering =['-id']

    def __str__(self):
        return self.rut
