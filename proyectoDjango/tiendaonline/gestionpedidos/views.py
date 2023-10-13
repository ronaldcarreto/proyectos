from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import articulos


# Create your views here.

def busqueda(request):

    return render(request, "busqueda.html")



def buscar(request):
        
        if request.GET["producto"]:
         
         producto=request.GET["producto"]   
         
         Articulos=articulos.objects.filter(nombre__icontains= producto)

         return render(request, "resultadobusqueda.html", {"articulos": articulos, "query": producto})


        else:
         mensaje= "no has introducido nada"

        return HttpResponse(mensaje)