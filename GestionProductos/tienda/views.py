from rest_framework import viewsets
from .models import Producto, Orden
from .serializers import ProductoSerializer, OrdenSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
from django.shortcuts import render, redirect
from .models import Producto

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', {})
    carrito[producto_id] = carrito.get(producto_id, 0) + 1
    request.session['carrito'] = carrito
    return redirect('listar_productos')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = Producto.objects.get(id=producto_id)
        productos.append({'producto': producto, 'cantidad': cantidad})
        total += producto.precio * cantidad

    return render(request, 'ver_carrito.html', {'productos': productos, 'total': total})

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if producto_id in carrito:
        del carrito[producto_id]
        request.session['carrito'] = carrito
    return redirect('ver_carrito')
