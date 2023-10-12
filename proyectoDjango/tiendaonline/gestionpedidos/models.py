from django.db import models

# Create your models here.




# ESTA APP SE DEBERA DECLARAR EN SETTINGS.PY  OPCION DE INSTALLED.APP   --ESTA SE ENCUENTRA LA CARPETA TIENDA ONLINE


#tabla de clientes
class clientes(models.Model):

    nombre=models.CharField(max_length=30)         #ingresara caracteres tipo texto de longitud 30
    #direccion=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50, verbose_name="La dirección")
    email=models.EmailField()                      #solo permitira ingresar email
    #email=models.EmailField(blank=True, null=True)      PARA QUE NO SEA OBLIGATORIO INGRESAR EMAIL 
    telefono=models.CharField(max_length=9)

    def __str__(self):
        return self.nombre              #para que al consultar los clientes en Django administration me aparezca los nombres en la vista general de clientes

#tabla de articulos
class articulos(models.Model):

    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

 #tabla de pedios
class pedidos(models.Model): 
    numero=models.IntegerField()
    fecha=models.DateField()                        #solo permitira ingresar texto tipo fecha
    entregado=models.BooleanField()                 #solo permitira ingresar dato tipo tru o false