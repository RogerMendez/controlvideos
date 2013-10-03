#encoding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext



from ventas.form import ClienteForm

def new_cliente(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = ClienteForm()
    return render_to_response('clientes/new_cliente.html', {'formulario' :formulario}, context_instance=RequestContext(request))






