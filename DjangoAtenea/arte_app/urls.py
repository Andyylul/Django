from django.urls import path
from .views import index,contactos,registrar,lana,lienzo,moldear,contra,crearla,crearli,creares,modificarla,modificarli,modificares,eliminarla,eliminarli,eliminares

urlpatterns = [
    path('', index, name='index'),
    path('contactos/', contactos, name='contactos'),
    path('lana/', lana, name='lana'),
    path('lienzo/', lienzo, name='lienzo'),
    path('moldear/', moldear, name='moldear'),
    path('registrar/', registrar, name='registrar'),
    path('contra/', contra, name='contra'),
    path('crearla/', crearla, name="crearla"),
    path('crearli/', crearli, name="crearli"),
    path('creares/', creares, name="creares"),
    path('modificarla/<id>', modificarla, name="modificarla"),
    path('modificarli/<id>', modificarli, name="modificarli"),
    path('modificares/<id>', modificares, name="modificares"),
    path('eliminarla/<id>', eliminarla, name="eliminarla"),
    path('eliminarli/<id>', eliminarli, name="eliminarli"),
    path('eliminares/<id>', eliminares, name="eliminares")
]
