from django.urls import path
from proyectowebapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/', views.registro, name="registro"),
    path('cursos/', views.cursos, name="cursos"),
    path('contacto/', views.cursos, name="contacto"),
    path('prueba/', views.prueba, name="prueba"),
]
