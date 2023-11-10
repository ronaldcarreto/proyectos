from django.shortcuts import render, HttpResponse
from .models import curso
from carro.carro import Carro



# Create your views here.


def catalogo(request):

    cursos= curso.objects.all()

    return render(request, "catalogo/catalogo.html", {"cursos":cursos})


def cart(request):

   

    return render(request, "catalogo/cart.html")

def cursoo(request):

    cursos= curso.objects.all()
    

    return render(request, "catalogo/curso.html", {"cursos":cursos})

def asignacion(request):

   

   return render(request, "catalogo/asignacion.html")