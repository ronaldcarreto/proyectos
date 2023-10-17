from django.urls import path
from . import views

app_name="carro"

urlpatterns = [
    path("agregar/<int:curso_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:curso_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:curso_id>/", views.restar_producto, name="restar"),
    path("limpiar/<int:curso_id>/", views.limpiar_carro, name="limpiar"),
    
]

