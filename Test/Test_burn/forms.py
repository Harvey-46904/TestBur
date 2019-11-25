from django.forms import ModelForm
from django import forms
from .models import Empresa
class EmpresaForms(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['Nombre', 'Direccion','email']