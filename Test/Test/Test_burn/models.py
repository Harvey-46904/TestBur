from django.db import models


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField('Nombre',max_length=150)
    Direccion=models.CharField('Dirección',max_length=150)
    email=models.EmailField('E-mail',max_length=200)
    '''image =models.ImageField('Author image',null=True,blank=True,upload_to='authors/')'''
    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
    def __str__(self):
        return self.Nombre


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    Nombres=models.CharField('Nombres',max_length=150)
    Apellidos=models.CharField('Nombres',max_length=150)
    Direccion=models.CharField('Dirección',max_length=150)
    email=models.EmailField('E-mail',max_length=200)
    empresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)
    '''image =models.ImageField('Author image',null=True,blank=True,upload_to='authors/')'''
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    def __str__(self):
        text=self.Nombres+' '+self.Apellidos
        return text
COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class MyModel(models.Model):
  color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')