from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def Display(request):
    return HttpResponse("<h1>Hola Mundo</h1>")