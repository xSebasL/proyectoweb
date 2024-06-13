from django.shortcuts import render
from tienda.models import Producto, CategoriaProd

# Create your views here.


def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()
    return render(request, "tienda/tienda.html", {'productos': productos, 'categorias': categorias})


def categoria(request, categoria_id):
    categoria = CategoriaProd.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = CategoriaProd.objects.all()
    return render(request, "tienda/categoria.html", {'categoria': categoria, 'productos': productos, 'categorias': categorias})
