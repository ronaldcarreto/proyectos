import datetime
from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("SALUDO")

def pruebahtml(request):

    prueba="<html><body><h1>ESTA ES UN PRUEBA CON HTML</html></body></h1>"
    return HttpResponse(prueba)


def pruebaplantilla(request):
    
    doc_externo=open("C:/Users/GEMELOS/Documents/proyectos/proyectoDjango/proyecto1/proyecto1/plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)

    return HttpResponse(documento)
   
def pruebaplantilla2(request):
    
    nombre="ronald"
    nombre2="eduardoo"
    apellido="carreto"
    hora=datetime.datetime.now()
    #clases":["mate","fisica", "electronica"]
    clases2:[]  #Lo coloque vacio para comprobar una funcion para que coloque un mensaje de que no hay clases disponibles



    doc_externo=open("C:/Users/GEMELOS/Documents/proyectos/proyectoDjango/proyecto1/proyecto1/plantillas/plantilla2.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona": nombre, "apellido_persona":apellido, "hora_actual":hora, "clases":["mate","fisica", "electronica"]})
    #ctx=Context({"nombre_persona": "ronald", "apellido_persona":"carreto"})   *otra forma de colocarlo*
    documento=plt.render(ctx)





    return HttpResponse(documento)









"""
def tiempo(request):

    timee=datetime.datetime.now()
    fecha ="<html><body><h1>ESTA ES UN PRUEBA CON HTML</html></body></h1>" % timee
   
    return HttpResponse(fecha)
    """
