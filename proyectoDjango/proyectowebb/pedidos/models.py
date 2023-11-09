from django.db import models
from tabnanny import verbose
from django.contrib.auth import get_user_model

from catalogo.models import curso
from carro.carro import Carro
from django.db.models import F, Sum, FloatField

# Create your models here.


User=get_user_model()

class Pedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
             
            total=Sum(F("precio"), output_field=FloatField())
                      

        )["total"]

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']


    def __str__(self):
        return str(self.id)  #aqui edite ------------------------------


class LineaPedido(models.Model):

        user=models.ForeignKey(User, on_delete=models.CASCADE)
        producto=models.ForeignKey(curso, on_delete=models.CASCADE)
        pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
        cantidad=models.IntegerField(default=1)
        created_at=models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'{self.producto.nombre}' #return f'{self.producto_id.nombre}'
        
        class Meta:
            db_table='lineapedidos'
            verbose_name='Linea Pedido'
            verbose_name_plural='Lineas Pedidos'
            ordering=['id']

            