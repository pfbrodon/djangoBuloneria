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