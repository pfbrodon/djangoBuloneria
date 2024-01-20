from django import forms
from django.forms import ModelForm
from .models import Producto
class NuevoForm(ModelForm):
    class Meta:
        model= Producto
        fields=('codigo', 'categoria' , 'marca' , 'descripcion' , 'cantidad' , 'utilidad' , 'precioCosto' )
        widgets ={
            'codigo': forms.NumberInput(attrs={'class': 'form-control','id':'codigo'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.Select(attrs={'class': 'form-select','id':'marca'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'id':'descripcion'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control','id':'cantidad'}),
            'utilidad': forms.Select(attrs={'class': 'form-select'}),
            'precioCosto': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields=('codigo', 'categoria' , 'marca' , 'descripcion' , 'cantidad' , 'utilidad' )
        
#class ProductoBusqueda(forms.Form):
#   nombre = forms.CharField(label='Buscar por nombre', max_length=100)
    
class ProductoBusqueda(forms.Form):
    descripcion = forms.CharField(
        max_length=100,
        #widget=forms.TextInput(attrs={'class': 'form-control'})
    )