from django import forms
from django.forms import ModelForm
from .models import Producto
class NuevoForm(ModelForm):
    class Meta:
        model= Producto
        fields=('codigo', 'categoria' , 'marca' , 'descripcion' , 'cantidad' , 'utilidad' , 'precioCosto' )
        widgets ={
            'codigo': forms.NumberInput(attrs={'class': 'form-control','id':'codigo','style': 'width: 150px'}),
            'categoria': forms.Select(attrs={'class': 'form-select','style': 'width: 220px'}),
            'marca': forms.Select(attrs={'class': 'form-select','id':'marca','style': 'width: 220px'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'id':'descripcion','style': 'width: 500px'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control','id':'cantidad','style': 'width: 150px'}),
            'utilidad': forms.Select(attrs={'class': 'form-select','style': 'width: 220px'}),
            'precioCosto': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 150px'}),
        }
        labels = {
            'precioCosto': 'Precio Costo',
        }
    def __init__(self, *args, **kwargs):
        super(NuevoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = 'Seleccione la categoría'
        self.fields['marca'].empty_label = 'Seleccione la marca'
        self.fields['utilidad'].empty_label = 'Seleccione la utilidad'


class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields=('codigo', 'categoria' , 'marca' , 'descripcion' , 'cantidad' , 'utilidad' ,'precioCosto')
        widgets ={
            'codigo': forms.NumberInput(attrs={'class': 'form-control','id':'codigo','style': 'width: 150px'}),
            'categoria': forms.Select(attrs={'class': 'form-select','style': 'width: 150px','placeholder': 'Seleccione la categoría'}),
            'marca': forms.Select(attrs={'class': 'form-select','id':'marca','style': 'width: 150px','placeholder': 'Seleccione la marca'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'id':'descripcion','style': 'width: 500px'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control','id':'cantidad','style': 'width: 150px'}),
            'utilidad': forms.Select(attrs={'class': 'form-select','style': 'width: 150px','placeholder': 'Seleccione la utilidad'}),     
            'precioCosto': forms.NumberInput(attrs={'class': 'form-select','style': 'width: 150px'}),            
        }
        labels = {
            'precioCosto': 'Precio Costo',
        }
            
class ProductoBusqueda(forms.Form):
    descripcion = forms.CharField(
        max_length=50,
        label= 'BUSQUEDA:',
        widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 400px;','placeholder':'ingrese la busqueda'})
    )