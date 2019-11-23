from django.forms import ModelForm

from .models import Empresa

class EmpresaForms(ModelForm):
    class Meta:
        model = Empresa
        fields = ['Nombre', 'Direccion','email']