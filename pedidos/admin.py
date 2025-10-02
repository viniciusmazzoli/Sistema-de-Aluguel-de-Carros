from django.contrib import admin
from .models import Pedido, Contrato

class ContratoInline(admin.StackedInline):
    model = Contrato
    can_delete = False
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'automovel', 'status', 'data_pedido')
    list_filter = ('status', 'data_pedido')
    search_fields = ('cliente__nome', 'automovel__placa')
    inlines = [ContratoInline]
    readonly_fields = ('data_pedido',)

admin.site.register(Contrato)
