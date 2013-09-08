#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from videos.forms import VideosForm, ImagenForm
from videos.models import Videos, Imagen


def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def new_video(request):
    if request.method =='POST' :
        formulario = VideosForm(request.POST, request.FILES)
        if formulario.is_valid() :
            titulo = formulario.cleaned_data['titulo']
            formato = formulario.cleaned_data['formato']
            cantidad = formulario.cleaned_data['cantidad']
            tipo = formulario.cleaned_data['tipo']
            sinopsis = formulario.cleaned_data['sinopsis']
            costo = formulario.cleaned_data['costo']

            Videos.objects.create(
                titulo = titulo,
                formato = formato,
                cantidad = cantidad,
                tipo = tipo,
                sinopsis = sinopsis,
                costo = costo,
                user = request.user,
            )
            return HttpResponseRedirect('/private')
    else:
        formulario = VideosForm()
    return render_to_response('Videos/new_video.html', {'formulario' :formulario}, context_instance=RequestContext(request))

def info_video(request, id_video):
    video = get_object_or_404(Videos, pk = id_video)
    imagenes = Imagen.objects.filter(video_id = id_video)
    return render_to_response('Videos/info_video.html', {'video' :video, 'imagenes' :imagenes}, context_instance=RequestContext(request))

def new_imagen(request, id_video):
    if request.method =='POST' :
        formulario = ImagenForm(request.POST, request.FILES)
        if formulario.is_valid() :
            #nombre = formulario.cleaned_data['nombre']
            #imagen = formulario.cleaned_data['imagen']
            img = formulario.save()
            img.video_id = id_video
            img.save()
            return HttpResponseRedirect('/video/info/' + id_video + '/')
    else:
        formulario = ImagenForm()
    return render_to_response('Videos/new_imagen.html', {'formulario' :formulario, 'id_video' :id_video}, context_instance=RequestContext(request))