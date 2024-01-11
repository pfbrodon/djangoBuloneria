from django.db import models
from django.utils import timezone

# Create your models here.
class Utilidad(models.Model):
    utilValor = models.FloatField()
    utilDescripcion = models.CharField(max_length = 150)
    
class Categoria(models.Model):
    catNom = models.CharField(max_length = 50)
    catDescripcion= models.CharField(max_length=100)
    
class Producto(models.Model):
    categoria = models.CharField(max_length = 150)
    marca = models.CharField(max_length = 150)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length = 150)
    cantidad = models.IntegerField()
    ultimoIngreso = models.DateTimeField(auto_now_add=False,default=timezone.now)
    precioCosto = models.FloatField(default=0.0)
    utilidad = models.FloatField(default=0.0)
    precioPublico= models.FloatField(default=0.0)
