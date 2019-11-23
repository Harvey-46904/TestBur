from django.shortcuts import render,redirect
from .forms import *
from .models import Empresa

def Home(request):
    return render(request,'index.html')

def CrearEmpresa(request):
    if request.method=='POST':
        genero_forms=EmpresaForms(request.POST)
        if genero_forms.is_valid():
            genero_forms.save()
            return redirect('index')
    else :
        genero_forms= EmpresaForms()
        return render(request,'Crear_empresa.html',{'empresa_form':genero_forms})

def ListarEmpresa(request):
    generos=Empresa.objects.all()
    return render(request,'listar_genero.html',{'generos':generos})