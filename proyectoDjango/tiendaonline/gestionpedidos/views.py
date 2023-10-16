from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionpedidos.forms import formulariocontacto

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

      miformulario=formulariocontacto(request.POST)
      
      if miformulario.is_valid():

        infform=miformulario.cleaned_data
        send_mail(infform['asunto'], infform['mensaje'], infform.get('email',' '),['gmlos2000@gmail.com'],)

      return render(request, "gracias.html")
      
    else:
       
       miformulario=formulariocontacto()

       return render(request, "formulariocontacto.html",{"form": miformulario})


        #subject=request.POST["asunto"]
        #message=request.POST["mensaje"]+ " " + request.POST["email"]
        #email_from=settings.EMAIL_HOST_USER
        #recipient_list=["kinkaku2000@gmail.com"]

        #send_mail(subject, message, email_from, recipient_list)


        #return render(request, "gracias.html")
        
    #return render(request, "contacto.html")
    