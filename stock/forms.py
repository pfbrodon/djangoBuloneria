from django import forms
from django.forms import ModelForm
from .models import Producto
class NuevoForm(ModelForm):
    class Meta:
        model= Producto
        fields=('codigo', 'categoria' , 'marca' , 'descripcion' , 'cantidad' , 'utilidad' , 'precioCosto' )
        widgets ={
            'codigo': forms.NumberInput(attrs={'class': 'form-control','id':'codigo','style': 'width: 150px;'}),
            'categoria': forms.Select(attrs={'class': 'form-select','style': 'width: 150px;'}),
            'marca': forms.Select(attrs={'class': 'form-select','id':'marca','style': 'width: 150px;'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'id':'descripcion','style': 'width: 500px;'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control','id':'cantidad','style': 'width: 150px;'}),
            'utilidad': forms.Select(attrs={'class': 'form-select','style': 'width: 150px;'}),
            'precioCosto': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 150px;'}),
            
        }
class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields=('codigo', 'categoria' , 'marca' , 'descripcion' , 'cantidad' , 'utilidad' ,'precioCosto')
        widgets ={
            'codigo': forms.NumberInput(attrs={'class': 'form-control','id':'codigo','style': 'width: 150px;'}),
            'categoria': forms.Select(attrs={'class': 'form-select','style': 'width: 150px;'}),
            'marca': forms.Select(attrs={'class': 'form-select','id':'marca','style': 'width: 150px;'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'id':'descripcion','style': 'width: 500px;'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control','id':'cantidad','style': 'width: 150px;'}),
            'utilidad': forms.Select(attrs={'class': 'form-select','style': 'width: 150px;'}),     
            'precioCosto': forms.NumberInput(attrs={'class': 'form-select','style': 'width: 150px;'}),            
        }
            
class ProductoBusqueda(forms.Form):
    descripcion = forms.CharField(
        max_length=50,
        label= 'BUSQUEDA:',
        widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 400px;'})
    )