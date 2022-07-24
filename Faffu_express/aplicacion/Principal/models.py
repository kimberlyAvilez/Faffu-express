from datetime import date, datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    apellido=models.CharField(max_length=50, verbose_name='Apellido')
    telefono=models.PositiveIntegerField()
    email=models.EmailField(max_length=80)
        
    def __str__(self, nombre, apellido,telefono,email):
       self.nombre = nombre
       self.apellido = apellido
       self.telefono = telefono
       self.email = email

class pedido(models.Model):
    id_pedido=models.AutoField(primary_key=True)
    fecha=models.TimeField()
    precio_subTotal=models.PositiveSmallIntegerField()
    duracion=models.IntegerField()

    

class aperitivos(models.Model):
    id_aperitivo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    tipo=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=100)
    cantidad_aperitivo=models.PositiveSmallIntegerField()
    precio=models.PositiveIntegerField()
    imagen=models.ImageField()

class pedido_aperitivo(models.Model):
    id_pedAperitivo=models.AutoField(primary_key=True)
    pedido=models.ForeignKey(pedido, on_delete=models.CASCADE)
    cantidad=models.PositiveSmallIntegerField()
    aperitivos=models.ForeignKey(aperitivos, on_delete=models.CASCADE)

class bebidas(models.Model):
    id_bebidas=models.AutoField(primary_key=True)
    nombre_bebida=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=100)
    tipo=models.CharField(max_length=25)
    cantidad=models.PositiveSmallIntegerField
    tamaño=models.CharField(max_length=15)
    precio=models.PositiveIntegerField()
    imagen=models.ImageField()

class bebidas_pedido(models.Model):
    id_pedBebidas=models.AutoField(primary_key=True)
    # pedido=models.ForeignKey(pedido, on_delete=models.CASCADE)
    cantidad=models.PositiveSmallIntegerField()
    bebidas=models.ForeignKey(bebidas, on_delete=models.CASCADE)



class facturas(models.Model):
    id_facturas=models.AutoField(primary_key=True)
    fecha=models.TimeField()
    descuento=models.DecimalField(max_digits = 5, decimal_places = 0)
    forma_pago=models.IntegerField()
    iva=models.DecimalField(max_digits = 5, decimal_places = 0)
    precio_Total=models.IntegerField()
    Cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido=models.ForeignKey(pedido, on_delete=models.CASCADE)
 
    

    


