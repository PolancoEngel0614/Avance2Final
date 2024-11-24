from django.contrib import admin
from .models import Productos 
# Register your models here.
#admin.site.register(Productos)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('CodigoProducto', 'DescripcionProducto', 'Estatus')

admin.site.register(Productos, ProductosAdmin)