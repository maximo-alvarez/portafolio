from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Usuario(AbstractUser):
    cedula = models.CharField(max_length=10, null=True, blank=True)
    celular = models.CharField(max_length=10, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    foto = models.ImageField(upload_to='usuario/%Y/%m', default='static/img/user.jpg', null=True, blank=True)
    url_git = models.CharField(max_length=250, null=True, blank=True)
    url_linkedin = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username

# Create your models here.
class Mensaje(models.Model):
    asunto = models.CharField(max_length=100, null=True, blank=True)
    correo = models.CharField(max_length=30, null=True, blank=True)
    mensaje = models.CharField(max_length=500, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    usuario = models.ForeignKey(Usuario, related_name="mensajes", on_delete=models.PROTECT)


@receiver(post_save, sender=Usuario)
def usuario_postsave_handler(sender, instance, **kwargs):
    if kwargs["created"]:
        usuario = instance
        usuario.groups.add(Group.objects.get(name='usuario_github'))
        usuario.is_staff = True
        usuario.save()