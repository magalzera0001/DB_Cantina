from django.contrib import admin
from .models import Produto, Usuario, Pedido, ItemPedido

# Registrar modelos no painel do Django Admin
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
