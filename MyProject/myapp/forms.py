from django import forms
from django.forms import ModelForm
from myapp.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name' : 'nome',
            'description': 'descricao',
            'price': 'preco',
            'image': 'imagem',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Tênis'
                }
            ),
            'descripion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Marca Nike'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 100.00'
                }
            ),
            'image': forms.ClearableFileInput(),
        }