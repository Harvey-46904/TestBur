from django.shortcuts import render,redirect
from .forms import *
from .models import *

class CreateMyModelView(CreateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'myapp/template.html'
    success_url = 'myapp/success.html'