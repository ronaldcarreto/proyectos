from django.shortcuts import render
from .carro import Carro
from catalogo.models import curso
from django.shortcuts import redirect

# Create your views here.


def agregar_producto(request, curso_id):
        
        carro = Carro(request)

        cursos= curso.objects.get(id=curso_id)

        carro.agregar(curso = cursos)  
         
        return redirect("catalogo") 


def eliminar_producto(request, curso_id):
        carro=carro(request)

        cursos=curso.objects.get(id= curso_id)

        carro.eliminar(curso=cursos)   

        return redirect("catalogo") 


def limpiar_carro(request, producto_id):
    
    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("catalogo") 