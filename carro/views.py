from django.shortcuts import render, redirect
from carro.carro import Carro
from tienda.models import Producto


def agregar_producto(request, producto_id):
    carro = Carro(request=request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")


def eliminar_producto(request, producto_id):
    carro = Carro(request=request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")


def restar_producto(request, producto_id):
    carro = Carro(request=request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")


def limpiar_carro(request):
    carro = Carro(request=request)
    carro.limpiar_carro()
    return redirect("tienda")
