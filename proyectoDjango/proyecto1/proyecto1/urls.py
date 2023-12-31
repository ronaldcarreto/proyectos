"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto1.views import saludo,pruebahtml, pruebaplantilla,pruebaplantilla2,pruebaplan2,  pruebaplan3, curso, curso2 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asdf/', saludo),
    path('htmlprueba/', pruebahtml),
    path('pruebaplan/', pruebaplantilla),
    path('pruebaplan2/', pruebaplantilla2),
    path('pruebaplan2/', pruebaplan2),
    path('pruebaplan3/', pruebaplan3),
    path('pruebaplan3/', pruebaplan3),
    path('curso/', curso),
    path('curso2/', curso2),
]
