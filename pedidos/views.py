from django.shortcuts import render, redirect
from carro.context_processor import importe_total_carro
from pedidos.models import Pedido, LineaPedido
from tienda.models import Producto
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages


@login_required(login_url="/authentication/login/")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            user=request.user,
            producto=Producto.objects.get(id=key),
            pedido=pedido,
            cantidad=value["cantidad"]
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    imprimir_pedido(
        request=request,
        nombre_usuario=request.user.username,
        pedido=pedido,
        lineas_pedido=lineas_pedido
    )
    messages.success(request, "Pedido realizado correctamente")
    carro.limpiar_carro()
    return redirect("tienda")


def imprimir_pedido(request, nombre_usuario, pedido, lineas_pedido):
    with open(f"pedidos/facturas_pedidos/{pedido.id}.txt", "w") as file_pedido:
        file_pedido.write(f"Nombre de usuario: {nombre_usuario}\n")
        file_pedido.write(f"ID pedido: {pedido.id}\n")
        file_pedido.write(f"Fecha pedido: {pedido.created_at}\n")
        file_pedido.write("Productos:\n")
        for linea_pedido in lineas_pedido:
            file_pedido.write(
                f"""Producto: {
                    linea_pedido.producto.nombre} --- Cantidad: {linea_pedido.cantidad} --- Precio: {linea_pedido.cantidad*linea_pedido.producto.precio}\n"""
            )
        file_pedido.write(
            f"Total: {importe_total_carro(request)["importe_total_carro"]}\n")
        file_pedido.close()
