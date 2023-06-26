from django.shortcuts import render, redirect
from .models import ProductosLana,ProductosLienzo,ProductosEscultura
from .forms import  RegistroUserForm,ProductosLanaForm,ProductosLienzoForm,ProductosEsculturaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import os
def index(request):
    return render(request, 'index.html')

def contactos(request):
    return render(request, 'contactos.html')


def lana(request):
    productos = ProductosLana.objects.all()
    datos={
        'productos':productos
    }
    return render(request, 'lana.html',datos)


def lienzo(request):
    productos = ProductosLienzo.objects.all()
    datos={
        'productos':productos
    }
    return render(request, 'lienzo.html',datos)

def moldear(request):
    productos = ProductosEscultura.objects.all()
    datos={
        'productos':productos
    }
    return render(request, 'moldear.html',datos)

def registrar(request):
    data={
        'form':RegistroUserForm()
     }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
             formulario.save()
             user = authenticate(username=formulario.cleaned_data["username"], 
                  password=formulario.cleaned_data["password1"])
             login(request,user)
             return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)

def contra(request):
    return render(request, 'contra.html')

@login_required
def crearla(request):
    if request.method=="POST":
        form = ProductosLanaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()     #similar al insert
            return redirect('index')
    else:
        form=ProductosLanaForm()
    return render(request, 'crearla.html', {'form':form})

@login_required
def crearli(request):
    if request.method=="POST":
        form = ProductosLienzoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()     #similar al insert
            return redirect('index')
    else:
        form=ProductosLienzoForm()
    return render(request, 'crearli.html', {'form':form})

@login_required
def creares(request):
    if request.method=="POST":
        form = ProductosEsculturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()     #similar al insert
            return redirect('index')
    else:
        form=ProductosEsculturaForm()
    return render(request, 'creares.html', {'form':form})

@login_required
def modificarla(request, id):
    producto = ProductosLana.objects.get(dila=id)
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(producto.imagen)>0:
                os.remove(producto.imagen.path)
            producto.imagen=request.FILES['imagen']
        producto.nombre=request.POST.get('nombre')
        producto.descripcion=request.POST.get('descripcion')
        producto.precio=request.POST.get('precio')
        producto.save()
        return redirect('lana')
    datos = {
        'form': ProductosLanaForm(request.POST,request.FILES,instance=producto)
    }
    return render(request, 'modificar.html', datos)

@login_required
def modificarli(request, id):
     producto = ProductosLienzo.objects.get(dili=id)
     if request.method=='POST':
          if len(request.FILES)!=0:
               if len(producto.imagen)>0:
                    os.remove(producto.imagen.path)
               producto.imagen=request.FILES['imagen']
          producto.nombre=request.POST.get('nombre')
          producto.descripcion=request.POST.get('descripcion')
          producto.precio=request.POST.get('precio')
          producto.save()
          return redirect('lienzo')
     datos = {
          'form': ProductosLienzoForm(request.POST,request.FILES,instance=producto)
     }
     return render(request, 'modificar.html', datos)

@login_required
def modificares(request, id):
     producto = ProductosEscultura.objects.get(dies=id)
     if request.method=='POST':
          if len(request.FILES)!=0:
               if len(producto.imagen)>0:
                    os.remove(producto.imagen.path)
               producto.imagen=request.FILES['imagen']
          producto.nombre=request.POST.get('nombre')
          producto.descripcion=request.POST.get('descripcion')
          producto.precio=request.POST.get('precio')
          producto.save()
          return redirect('moldear')
     datos = {
          'form': ProductosEsculturaForm(request.POST,request.FILES,instance=producto)
     }
     return render(request, 'modificar.html', datos)
@login_required
def eliminarla(request, id):
    productoEliminado = ProductosLana.objects.get(dila=id)
    productoEliminado.delete()
    return redirect ('index')
@login_required
def eliminarli(request, id):
    productoEliminado = ProductosLienzo.objects.get(dili=id)
    productoEliminado.delete()
    return redirect ('index')
@login_required
def eliminares(request, id):
    productoEliminado = ProductosEscultura.objects.get(dies=id)
    productoEliminado.delete()
    return redirect ('index')