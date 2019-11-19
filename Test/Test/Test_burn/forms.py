from django import forms
from .models import *

class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['color']