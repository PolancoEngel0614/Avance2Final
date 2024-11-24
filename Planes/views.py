from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Productos
# Create your views here.


"""def Productos (request):
    #return HttpResponse('Nuestra Primera Vista!')
    misProductos = Productos.objects.all().values()
    template = loader.get_template('Productos.html')
    Context = {
        'misProductos': misProductos 
    }
    return HttpResponse(template.render(Context, request))
"""
def Bienvenida(request):
    template = loader.get_template('MiPrimerTemplate.html')
    return HttpResponse(template.render())


