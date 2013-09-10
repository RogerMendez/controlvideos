#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from videos.forms import VideosForm, ImagenForm, ActorForm
from videos.models import Videos, Imagen, Actor, Actor_Video


def home(request):
    videos = Videos.objects.filter(cantidad__gte = 1)
    return render_to_response('index.html',{'videos' :videos}, context_instance=RequestContext(request))

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

def option_video(request):
    videos = Videos.objects.filter(cantidad__gte = 1, user=request.user)
    return render_to_response('Videos/option_video.html', {'videos' :videos}, context_instance=RequestContext(request))

def info_video(request, id_video):
    video = get_object_or_404(Videos, pk = id_video)
    imagenes = Imagen.objects.filter(video_id = id_video)
    q1 = Actor_Video.objects.filter(video_id = id_video)
    q2 = q1.values('actor_id')
    actores = Actor.objects.filter(id__in=q2)
    return render_to_response('Videos/info_video.html', {'video' :video, 'imagenes' :imagenes, 'actores' :actores}, context_instance=RequestContext(request))

def new_imagen(request, id_video):
    if request.method =='POST' :
        formulario = ImagenForm(request.POST, request.FILES)
        if formulario.is_valid() :
            img = formulario.save()
            img.video_id = id_video
            img.save()
            return HttpResponseRedirect('/video/info/' + id_video + '/')
    else:
        formulario = ImagenForm()
    return render_to_response('Videos/new_imagen.html', {'formulario' :formulario, 'id_video' :id_video}, context_instance=RequestContext(request))

def new_actor(request, id_video):
    if request.method =='POST' :
        formulario = ActorForm(request.POST, request.FILES)
        if formulario.is_valid() :
            formulario.save()
            return HttpResponseRedirect('/video/info/'+id_video+'/')
    else:
        formulario = ActorForm()
    return render_to_response('Videos/new_actor.html', {'formulario' :formulario}, context_instance=RequestContext(request))

def show_actores(request, id_video):
    video = get_object_or_404(Videos, pk = id_video)
    q1 = Actor_Video.objects.filter(video_id = id_video)
    q2 = q1.values('actor_id')
    actores = Actor.objects.exclude(id__in=q2)
    return render_to_response('Videos/add_actor.html', {'video' :video, 'actores' :actores}, context_instance=RequestContext(request))

def add_actor(request, id_video,id_actor):
    Actor_Video.objects.create(
        video_id = id_video,
        actor_id = id_actor,
    )
    return HttpResponseRedirect('/video/info/'+id_video+'/')