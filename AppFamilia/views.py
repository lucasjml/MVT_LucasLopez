from multiprocessing import context
from django.shortcuts import render
from .models import Familia
from datetime import date
from django.db import models

# Create your views here.
def familia(request):
    return render(request, 'familia.html', context={})
    

"""def crear_familia(request):
    integrante = Familia.objects.create(
        nombre = "carlos",
        apellido = "peralta",
        dni = 550000222,
        fecha_nacimiento = date(year=2000, month=12, day=30))
    context = {'integrante': integrante}
    return render(request, 'familia.html', context)
        """

def mostrar_familia(request):
    integrantes = Familia.objects.all()
    context ={'integrantes' : integrantes}
    return render(request,'familia.html',context)