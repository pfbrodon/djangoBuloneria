from django.contrib import admin
from .models import Producto, Categoria, Utilidad
# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Utilidad)