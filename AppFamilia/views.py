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
        nombre = "Lucas",
        apellido = "Lopez",
        dni = 27319224,
        fecha_nacimiento = date(year=1979, month=05, day=01))
    context = {'integrante': integrante}
    return render(request, 'familia.html', context) #for template
        """

def mostrar_familia(request):
    integrantes = Familia.objects.all()
    context ={'integrantes' : integrantes}
    return render(request,'familia.html',context)