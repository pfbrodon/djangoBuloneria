from django.db import models

# Create your models here.
class Utilidad(models.Model):
    utilValor = models.FloatField()
    utilDescripcion = models.CharField(max_length = 100)
    
class Categorias (models.Model):
    catNom = models.CharField(max_length = 50)
    catDescripcion= models.CharField(max_length=100)
    
class Marcas(models.Model):
    marcaNom = models.CharField(max_length = 50)
    marcaDescripcion= models.CharField(max_length=100)
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length = 150)
    cantidad = models.IntegerField()
    precioCosto = models.FloatField(default=0.0)
    utilidad = models.ForeignKey(Utilidad, on_delete=models.CASCADE)
    precioPublico= models.FloatField(default=0.0)

def __str__(self):
        return self.title +'-by '+ self.user.username #muestra el titulo de la tarea en la administracion de django