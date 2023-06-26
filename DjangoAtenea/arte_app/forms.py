from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import ProductosLana, ProductosLienzo,ProductosEscultura
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProductosLanaForm(forms.ModelForm):
    class Meta:
        model = ProductosLana        
        fields = ['dila', 'nombre', 'descripcion','precio', 'imagen']
        labels = {                
            'dila': 'Id',
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
            'precio':'Precio', 
            'imagen':'Imagen'
        }
        widgets = {
            'dila' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese id del producto',
                    'id':'dila',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre del producto',
                    'id':'nombre',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripción del producto',
                    'id':'descripcion',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese precio del producto',
                    'id':'precio',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
        }

class ProductosLienzoForm(forms.ModelForm):
    class Meta:
        model = ProductosLienzo        
        fields = ['dili', 'nombre', 'descripcion','precio', 'imagen']
        labels = {                
            'dili': 'Id',
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
            'precio':'Precio', 
            'imagen':'Imagen'
        }
        widgets = {
            'dili' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese id del producto',
                    'id':'dili',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre del producto',
                    'id':'nombre',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripción del producto',
                    'id':'descripcion',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese precio del producto',
                    'id':'precio',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
        }

class ProductosEsculturaForm(forms.ModelForm):
    class Meta:
        model = ProductosEscultura        
        fields = ['dies', 'nombre', 'descripcion','precio', 'imagen']
        labels = {                
            'dies': 'Id',
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
            'precio':'Precio', 
            'imagen':'Imagen'
        }
        widgets = {
            'dies' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese id del producto',
                    'id':'dies',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre del producto',
                    'id':'nombre',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripción del producto',
                    'id':'descripcion',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese precio del producto',
                    'id':'precio',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),
        }