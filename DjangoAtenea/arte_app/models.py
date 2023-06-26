from django.db import models

# Create your models here.
class ProductosLana(models.Model):
    dila = models.CharField(primary_key=True,max_length=5,verbose_name="Dila")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    precio = models.IntegerField(blank=True,verbose_name="Precio") 
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="Imagen")

    def __str__(self):
        return self.dila

class ProductosLienzo(models.Model):
    dili = models.CharField(primary_key=True,max_length=5,verbose_name="Dili")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    precio = models.IntegerField(blank=True,verbose_name="Precio") 
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="Imagen")

    def __str__(self):
        return self.dili

class ProductosEscultura(models.Model):
    dies = models.CharField(primary_key=True,max_length=5,verbose_name="Dies")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    precio = models.IntegerField(blank=True,verbose_name="Precio") 
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="Imagen")

    def __str__(self):
        return self.dies