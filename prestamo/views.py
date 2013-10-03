from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from videos.models import Videos
from prestamo.models import Prestamo, DetallePrestamo
from ventas.models import Cliente

def new_prestamo(request, prestamo):
	if int(prestamo) == 0:
		pres = Prestamo.objects.create(
				usuario = request.user,
				)
		prestamo = pres.id
	q1 = Videos.objects.filter(user = request.user)
	q2 = DetallePrestamo.objects.filter(prestamo_id = int(prestamo))
	q3 = q2.values('video_id')
	videos_prestamo = q1.filter(id__in = q3)
	videos = q1.filter(cantidad__gte = 1).exclude(id__in = q3)
	return render_to_response('prestamo/add_video.html',
		 		{'videos' :videos, 'prestamo_id' :prestamo, 'videos_prestamo' :videos_prestamo},
	 			context_instance=RequestContext(request))

def add_video(request, prestamo_id, video_id):
	DetallePrestamo.objects.create(
		video_id = int(video_id),
		prestamo_id = int(prestamo_id),
		)
	return HttpResponseRedirect('/prestamo/videos/add/'+str(prestamo_id)+'/')

def delete_video(request, prestamo_id, video_id):
	q1 = DetallePrestamo.objects.get(prestamo_id = prestamo_id, video_id=video_id)
	q1.delete()
	return HttpResponseRedirect('/prestamo/videos/add/'+str(prestamo_id)+'/')

def select_cliente(request, prestamo_id):
	clientes =  Cliente.objects.all()
	return render_to_response('prestamo/select_cliente.html',
		{'clientes' :clientes, 'prestamo_id' :prestamo_id},
		context_instance=RequestContext(request))

def confirm_prestamo(request, prestamo_id, cliente_id):
	q1 = get_object_or_404(Prestamo, pk = prestamo_id)
	q1.estado = True
	q1.cliente_id = cliente_id
	q1.save()
	return HttpResponseRedirect('/')

def cancel_prestamo(request, prestamo_id):
	q1 = DetallePrestamo.objects.filter(prestamo_id = prestamo_id)
	for detalle in q1:
		DetallePrestamo.objects.get(prestamo_id = prestamo_id, video_id = detalle.video_id).delete()
	Prestamo.objects.get(pk = prestamo_id).delete()
	return HttpResponseRedirect('/')
