from django.urls import path
from .views import *
urlpatterns = [
  path('crear_genero/',CrearEmpresa,name ='Crear_Genero'),
  path('listar_genero',ListarEmpresa,name='listar_autor')
]