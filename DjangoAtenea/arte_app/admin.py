from django.contrib import admin
from .models import ProductosLana, ProductosLienzo,ProductosEscultura

# Register your models here.
admin.site.register(ProductosLana),
admin.site.register(ProductosLienzo),
admin.site.register(ProductosEscultura)