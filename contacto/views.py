from django.shortcuts import render, redirect
from contacto.forms import FormContacto

# Create your views here.


def contacto(request):
    form_contacto = FormContacto()
    print(request)
    if request.method == "POST":
        form_contacto = FormContacto(data=request.POST)
        if form_contacto.is_valid():
            nombre = request.POST["nombre"]
            email = request.POST["email"]
            contenido = request.POST["contenido"]
            print(nombre, email, contenido)
            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {"form_contacto": form_contacto})
