
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.catalogo, name="catalogo"),

    path('cart/', views.cart, name="cart"),

    path('cursoo/', views.cursoo, name="cursoo"),
    path('asignacion/', views.asignacion, name="asignacion"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
