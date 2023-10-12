from django.contrib import admin


from gestionpedidos.models import clientes, articulos, pedidos


class clientesAdmin(admin.ModelAdmin):                  #para que aparezca "nombre","direccion", "telefono" 
    list_display=("nombre","direccion", "telefono","email")     # en la vista general de clientes de Django administration
    search_fields=("nombre", "telefono")        #agrega casilla de busqueda de nombre y telefono

class articulosAdmin(admin.ModelAdmin):                  #para que aparezca "nombre","direccion", "telefono" 
    list_display=("nombre","seccion", "precio")     # en la vista general de clientes de Django administration
    search_fields=("nombre", "precio")        #agrega casilla de busqueda de nombre y telefono
    list_filter=("nombre", "precio",)


class pedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha", "entregado")                
    list_filter=("fecha",)
    date_hierarchy="fecha" #filtro de barra horizontal


# Register your models here.
admin.site.register(clientes, clientesAdmin)
admin.site.register(articulos,articulosAdmin)
admin.site.register(pedidos, pedidosAdmin)