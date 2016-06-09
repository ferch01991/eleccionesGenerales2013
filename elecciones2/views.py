from elecciones2.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def inicio(request):
	candidatos = Candidatos.objects.all()
	return render_to_response('inicio.html', {'candidatos':candidatos})

def cantones(request):
	cantones = Cantones.objects.all()
	return render_to_response('cantones.html', {'cantones':cantones})