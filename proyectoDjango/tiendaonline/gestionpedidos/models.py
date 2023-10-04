from django.db import models

# Create your models here.




# ESTA APP SE DEBERA DECLARAR EN SETTINGS.PY  OPCION DE INSTALLED.APP   --ESTA SE ENCUENTRA LA CARPETA TIENDA ONLINE


#tabla de clientes
class clientes(models.Model):

    nombre=models.CharField(max_length=30)         #ingresara caracteres tipo texto de longitud 30
    direccion=models.CharField(max_length=50)
    email=models.EmailField()                      #solo permitira ingresar email
    telefono=models.CharField(max_length=9)

#tabla de articulos
class articulos(models.Model):

    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

 #tabla de pedios
class pedidos(models.Model): 
    numero=models.IntegerField()
    fecha=models.DateField()                        #solo permitira ingresar texto tipo fecha
    entregado=models.BooleanField()                 #solo permitira ingresar dato tipo tru o false