from django.db import models

from videos.models import Videos
from ventas.models import Cliente
from django.contrib.auth.models import User

class Prestamo(models.Model):
    fecha_prestamo = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    usuario = models.ForeignKey(User)
    def __unicode__(self):
    	return self.cliente

class DetallePrestamo(models.Model):
	video = models.ForeignKey(Videos)
	prestamo = models.ForeignKey(Prestamo)
	def __unicode__(self):
		return self.cliente
	class Meta:
		ordering = ['video']
		verbose_name_plural = 'Detalle Prestamo'