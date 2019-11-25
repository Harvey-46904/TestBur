from django.urls import path
from .views import *
urlpatterns = [
  path('crear_genero/',CrearEmpresa,name ='Crear_Genero'),
  path('delete/<int:empresa_id>',BorrarEmpresa,name='delete'),
  path('edit/<int:empresa_id>',UpdateEmpresa,name='update')
]