from django.urls import path, include
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/', views.registro, name="registro"),
    path('cursos/', views.cursos, name="cursos"),
    path('contacto/', views.cursos, name="contacto"),
    path('prueba/', views.prueba, name="prueba"),
    path('catalogo/', include('catalogo.urls')),

    
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)