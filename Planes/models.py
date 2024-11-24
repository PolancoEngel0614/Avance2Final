from django.db import models

# Create your models here.

class Productos(models.Model):
    CodigoProducto = models.CharField(max_length=10)
    DescripcionProducto = models.CharField(max_length=255)
    Estatus = models.BooleanField()