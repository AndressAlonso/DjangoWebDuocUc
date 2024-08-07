from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now)
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.nombre
    
class Tipo_producto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.nombre
    
class Producto (models.Model):
    id = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey(to=Marca, on_delete=models.CASCADE)
    id_tipo_producto = models.ForeignKey(to=Tipo_producto,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255)
    precio = models.IntegerField()
    ram = models.CharField(max_length=80,default='No Registrado')
    procesador = models.CharField(max_length=80,default='No Registrado')
    almacenamiento = models.CharField(max_length=80,default='No Registrado')
    tamaño_pantalla = models.CharField(max_length=80,default='No Registrado')
    capacidad_bateria = models.CharField(max_length=80,default='No Registrado')
    color = models.CharField(max_length=80,default='No Registrado')
    def __str__(self):
        return self.descripcion


class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    