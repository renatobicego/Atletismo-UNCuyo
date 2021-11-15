from django.shortcuts import render

from .models import FotoUrl, Media, Prueba, Torneo

# Create your views here.

def index(request):
    return render(request, "uncuyo/index.html")

def sumate(request):
    return render(request, 'uncuyo/sumate.html')

def prueba(request, prueba):
    stuff = Prueba.objects.get(abr=prueba)
    media = Media.objects.get(prueba_id=stuff.id)
    return render(request, "uncuyo/prueba.html",{
        "prueba": stuff,
        "media": media
    })

def planes(request):
    return render(request, "uncuyo/planes.html")

def fotos(request):
    torneos = Torneo.objects.all()
    fotos = FotoUrl.objects.all()
    return render(request, "uncuyo/fotos.html", {
        "torneos": torneos,
        "fotos": fotos
    })