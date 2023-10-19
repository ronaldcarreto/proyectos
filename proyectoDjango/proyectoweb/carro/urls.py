from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name="Carro"


urlpatterns = [
    path("agregar/<int:curso_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:curso_id>/", views.eliminar_producto, name="eliminar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
