import datetime
from django.http import HttpResponse
from django.template import Template, Context
#from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def saludo(request):
    return HttpResponse("SALUDO")

def pruebahtml(request):

    prueba="<html><body><h1>ESTA ES UN PRUEBA CON HTML</html></body></h1>"
    return HttpResponse(prueba)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def pruebaplantilla(request):
    
    doc_externo=open("C:/Users/Alejandra/Documents/proyectos/proyectoDjango/proyecto1/proyecto1/plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)

    return HttpResponse(documento)
   

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def pruebaplantilla2(request):
    
    nombre="ronald"
    nombre2="eduardoo"
    apellido="carreto"
    hora=datetime.datetime.now()
    #clases":["mate","fisica", "electronica"]
    clases2:[]  #Lo coloque vacio para comprobar una funcion para que coloque un mensaje de que no hay clases disponibles



    doc_externo=open("C:/Users/Alejandra/Documents/proyectos/proyectoDjango/proyecto1/proyecto1/plantillas/plantilla2.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona": nombre, "apellido_persona":apellido, "hora_actual":hora, "clases":["mate","fisica", "electronica"]})
    #ctx=Context({"nombre_persona": "ronald", "apellido_persona":"carreto"})   *otra forma de colocarlo*
    documento=plt.render(ctx)


    return HttpResponse(documento)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#SIMPLIFICACION DE PLANTILLA 2
def pruebaplan2(request):
    
    nombre="ronald"
    nombre2="eduardoo"
    apellido="carreto"
    hora=datetime.datetime.now()
    #clases":["mate","fisica", "electronica"]
    clases2:[]  #Lo coloque vacio para comprobar una funcion para que coloque un mensaje de que no hay clases disponibles


    #doc_externo=open("C:/Users/Alejandra/Documents/proyectos/proyectoDjango/proyecto1/proyecto1/plantillas/plantilla2.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    
    #en vez de colocar las 3 lineas anteriores se configura la carpeta plantilla en settings.py en template y DIRS  
    doc_externo=get_template('plantilla2.html')

    #ctx=Context({"nombre_persona": nombre, "apellido_persona":apellido, "hora_actual":hora, "clases":["mate","fisica", "electronica"]})
    #documento=doc.render(ctx)     SE REMPLAZA POR LA LINEA DE ABAJO y el ctx se reemplaza por el contenido de la linea e arriba
    documento=doc_externo.render({"nombre_persona": nombre, "apellido_persona":apellido, "hora_actual":hora, "clases":["mate","fisica", "electronica"]})

    return HttpResponse(documento)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#SIMPLIFICACION DE prueba2plan
def pruebaplan3(request):
    
    nombre="ronald"
    #nombre2="Eduardo"
    apellido="carreto"
    
    
    hora=datetime.datetime.now()
    
    #doc_externo=get_template('plantilla2.html')
    #documento=doc_externo.render({"nombre_persona": nombre, "apellido_persona":apellido, "hora_actual":hora, "clases":["mate","fisica", "electronica"]})


  
    return render(request, "plantilla2.html", {"nombre_persona": nombre, "apellido_persona":apellido, "hora_actual":hora, "cursoss":["mate","fisica", "electronica","teo"]})


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def curso(request):

 hora=datetime.datetime.now()

 return render(request,"plantillahija.html",{"horaa":hora})


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def curso2(request):

 hora=datetime.datetime.now()

 return render(request,"plantillahija2.html",{"horaa":hora})















