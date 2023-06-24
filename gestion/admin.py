from django.contrib import admin
from .models import (#Imagen,
                     Categoria, Producto, Usuario)
# Register your models here.

# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
# class ImagenAdmin(admin.ModelAdmin):
#     list_display = ['nombre', 'id', 'nombre_tag']
#     ordering = ['-id']
#     readonly_fields = ['id','nombre_tag']
#     search_fields = ['nombre']

# admin.site.register(Imagen, ImagenAdmin)

