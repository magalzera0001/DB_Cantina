from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0  # Não exibe campos extras para novos itens por padrão

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_pedido', 'status', 'valor_total')
    list_filter = ('status', 'data_pedido')
    search_fields = ('usuario__username', 'id')  # Permite buscar por nome de usuário ou ID do pedido
    inlines = [ItemPedidoInline]


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido) # Pode ser registrado, mas geralmente é gerenciado via InlineAdmin
