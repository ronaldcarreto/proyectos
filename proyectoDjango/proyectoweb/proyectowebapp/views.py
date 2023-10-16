from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.


def home(request):

    return render(request, "proyectowebapp/home.html")

def prueba(request):

    return render(request, "proyectowebapp/prueba.html")

def registro(request):

    return render(request, "proyectowebapp/registro.html")


def cursos(request):

    return render(request, "proyectowebapp/cursos.html")

def contacto(request):

    return render(request, "proyectowebapp/contacto.html")