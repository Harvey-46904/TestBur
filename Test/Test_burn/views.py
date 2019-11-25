from django.shortcuts import redirect, render
from .models import *
from .forms import *


def Home(request):
    return render(request,'index.html')

def CrearEmpresa(request):
    if request.method=='POST':
        genero_forms=EmpresaForms(request.POST)
        if genero_forms.is_valid():
            genero_forms.save()
            return redirect('/Test_burn/crear_genero/')
    else :
        genero_forms= EmpresaForms()
        empre=Empresa.objects.all()
        return render(request,'Crear_empresa.html',{'empresa_form':genero_forms,'empres':empre})

def BorrarEmpresa(request, empresa_id):
    instancia = Empresa.objects.get(id=empresa_id)
    instancia.delete()
    return redirect('/Test_burn/crear_genero/')
def UpdateEmpresa(request, empresa_id):
    instancia = Empresa.objects.get(id=empresa_id)
    form = EmpresaForms(instance=instancia)
    if request.method == "POST":
        form = EmpresaForms(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "Editar_empresa.html", {'form': form})