from django.shortcuts import render
from carro.carro import Carro


def home(request):
    carro = Carro(request)
    return render(request, "proyectowebapp/home.html")
