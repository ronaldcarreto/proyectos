from django.contrib import admin
from .models import curso
# Register your models here.


class cursooadmin(admin.ModelAdmin):

    readonly_fields=("creacion", "update")

    


admin.site.register(curso, cursooadmin)