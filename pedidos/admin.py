from django.contrib import admin
from .models import Pedido, LineaPedido


class AdminPedido(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class AdminLineaPedido(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(Pedido, AdminPedido)
admin.site.register(LineaPedido, AdminLineaPedido)
