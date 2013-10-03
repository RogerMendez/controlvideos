#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Videos(models.Model):
    titulo = models.CharField(max_length=500, verbose_name='Ingrese El Titlulo del Video')
    formato_video = (
        ('DVD', 'DVD'),
        ('BLUE-RAY', 'BLUE-RAY'),
    )
    formato = models.CharField(max_length=10, choices=formato_video, verbose_name="Seleccione El Formato del Video")
    cantidad = models.IntegerField(default='1',verbose_name='Ingrese La Cantidad De Videos')
    tipo_video=(
        ('ACCION', 'ACCIÓN'),
        ('DRAMA', 'DRAMA'),
        ('FICCION', 'FICCIÓN'),
        ('TERROR', 'TERROR'),
        ('COMEDIA', 'COMEDIA'),
        ('DOCUMENTAL', 'DOCUMENTAL'),
    )
    tipo = models.CharField(max_length=20, choices=tipo_video, verbose_name='Seleccione El Tipo de Video')
    sinopsis = models.TextField(blank=True, null=True, verbose_name='Ingrese La Sinopsis Del Video')
    costo = models.FloatField(verbose_name='Registre El Costo Del Video')
    fecha_registro = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.titulo
    class Meta:
        ordering = ["titulo"]
        verbose_name_plural = "Videos"

class Imagen(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Ingrese El Nombre de La Imagen")
    imagen = models.ImageField(upload_to='imagenes', verbose_name="Seleccionar Imagen")
    fecha_registro = models.DateField(auto_now_add=True)
    video = models.ForeignKey(Videos, blank=True, null=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['fecha_registro']
        verbose_name_plural = "Imagenes"

class Actor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de Actor')
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Actores'

class Actor_Video(models.Model):
    video = models.ForeignKey(Videos)
    actor = models.ForeignKey(Actor)
    def __unicode__(self):
        return self.actor