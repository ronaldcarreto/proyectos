from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import articulos


# Create your views here.

def busqueda(request):

    return render(request, "busqueda.html")



def buscar(request):
        
    if request.GET["producto"]:
         
        articulo_bd = request.GET["producto"]

        articuloss = articulos.objects.filter(nombre__icontains=articulo_bd)
        
        return render(request,"resultadobusqueda.html", {"articulos":articuloss, "query":articulo_bd})

    else:     
        mensaje= "no has introducido nada"

    return HttpResponse(mensaje)



def contacto(request):

    if request.method=="POST":
        return render(request, "gracias.html")
        
    return render(request, "contacto.html")