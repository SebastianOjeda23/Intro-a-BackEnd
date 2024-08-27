from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import datetime

# Create your views here.

def Display(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def Display2(request):
    dt = datetime.datetime.now()
    x = "<b>Fecha y hora actual: </b>" +str(dt)
    return HttpResponse(x)

def Intro1(request):
    txt = "<h1>Bienvenido</h1>"
    txt += "<label>Nombre de usuario.</label>"
    txt += "<input type='text'><br>"
    txt += "<label>Contraseña.</label>"
    txt += "<input type='password'><br>"
    txt += "<button type='button'>Enviar</button>"
    return HttpResponse(txt)