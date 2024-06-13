from django.shortcuts import render
from blog.models import Post, Categoria


def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "blog/blog.html", {'posts': posts, 'categorias': categorias})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    categorias = Categoria.objects.all()
    return render(request, "blog/categoria.html", {'categoria': categoria, 'posts': posts, 'categorias': categorias})
