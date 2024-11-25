from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def Productos(request):
    return HttpResponse("Nuestra primera vista!")

def Asignacion (request):
    template = loader.get_template('AsignacionHTML.html')
    return HttpResponse(template.render())