from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return HttpResponse("hola mundo")

def vader(request):
    return HttpResponse("<h1>this is dave vader</h1>")

def starwars(request, nombre):
    return HttpResponse(f"Hola {nombre} saludos !!!")
