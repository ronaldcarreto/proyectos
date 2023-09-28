import datetime
from django.http import HttpResponse



def saludo(request):
    return HttpResponse("SALUDO")

def pruebahtml(request):

    prueba="<html><body><h1>ESTA ES UN PRUEBA CON HTML</html></body></h1>"
    return HttpResponse(prueba)






"""
def tiempo(request):

    timee=datetime.datetime.now()
    fecha ="<html><body><h1>ESTA ES UN PRUEBA CON HTML</html></body></h1>" % timee
   
    return HttpResponse(fecha)
    """
