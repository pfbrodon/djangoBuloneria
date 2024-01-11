from django.forms import ModelForm
from .models import Producto
class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields=['codigo', 'categoria' , 'marca' , 'descripcion' , 'cantidad' , 'ultimoIngreso' , 'precioCosto' , 'utlidad']