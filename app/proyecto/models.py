from django.db import models

from app.seguridad.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=250)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=1250)
    foto = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    # imagen = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    foto = models.ImageField(upload_to='proyecto/%Y/%m', null=True, blank=True)
    url_git = models.CharField(max_length=250, null=True, blank=True)
    url_proyecto = models.CharField(max_length=250, null=True, blank=True)

    categoria = models.ForeignKey(Categoria, related_name="proyectos", on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, related_name="proyectos", on_delete=models.PROTECT)


class Habilidad(models.Model):
    nombre = models.CharField(max_length=250)
    porcentaje = models.PositiveSmallIntegerField(default=0, null=True, blank=True)

    usuario = models.ForeignKey(Usuario, related_name="habilidades", on_delete=models.PROTECT)


