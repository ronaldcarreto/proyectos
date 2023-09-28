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
   


"""
def tiempo(request):

    timee=datetime.datetime.now()
    fecha ="<html><body><h1>ESTA ES UN PRUEBA CON HTML</html></body></h1>" % timee
   
    return HttpResponse(fecha)
    """
