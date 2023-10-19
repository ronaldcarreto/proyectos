from django.shortcuts import render
from .models import curso
from django.shortcuts import redirect

#from .carro import Carro

# Create your views here.


def catalogo(request):

    cursos= curso.objects.all()

    return render(request, "catalogo/catalogo.html", {"cursos":cursos})

def cart(request):

    return render(request, "catalogo/cart.html")
