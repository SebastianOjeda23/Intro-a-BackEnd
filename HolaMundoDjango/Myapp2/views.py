from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

def bienvenio(response):
    x = "Segunda app en funcionamiento"
    return HttpResponse(x)