from django.shortcuts import render
from .carro import carro
from catalogo.models import curso
from django.shortcuts import redirect

# Create your views here.


def agregar_producto(request, curso_id):
    
    carro=carro(request)

    curso=curso.objects.get(id=curso_id)

    carro.agregar(curso=curso)   

    return redirect("catalogo") 


def eliminar_producto(request, curso_id):
    carro=carro(request)

    curso=curso.objects.get(id=curso_id)

    carro.eliminar(curso=curso)   

    return redirect("catalogo") 


def restar_producto(request, curso_id):
    carro=carro(request)

    curso=curso.objects.get(id=curso_id)

    carro.restar_producto(curso=curso)   

    return redirect("catalogo") 


def limpiar_carro(request, curso_id):
    carro=carro(request)

    carro.limpiar_carro() 

    return redirect("catalogo") 