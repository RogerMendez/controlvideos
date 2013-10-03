from django.db import models

from videos.models import Videos

class Cliente(models.Model):
    ci_nit = models.IntegerField(verbose_name="Ingrese El NIT o CI")
    nombre = models.CharField(max_length=100, verbose_name='Registre el Nombre')
    email = models.EmailField(verbose_name='Correo Electronico')
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['ci_nit']
        verbose_name_plural = "Clientes"

class Venta(models.Model):
    costo_total = models.FloatField()
    fecha_venta = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    def __unicode__(self):
        return self.cliente.nombre

    class Meta:
        ordering = ['fecha_venta']
        verbose_name_plural = "Ventas"

class Detalle(models.Model):
    cantidad = models.IntegerField()
    costo_video = models.FloatField()
    video = models.ForeignKey(Videos)
    def __unicode__(self):
        return self.video.titulo
    class Meta:
        verbose_name_plural = "Detalle Venta"