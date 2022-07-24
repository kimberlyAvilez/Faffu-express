from django.db import models

# Create your models here.

class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    apellido=models.CharField(max_length=50, verbose_name='Apellido')
    telefono=models.PositiveIntegerField()
    email=models.EmailField(max_length=80)