from django.contrib import admin
from .models import Cliente, Rendimento

class RendimentoInline(admin.TabularInline):
    model = Rendimento
    extra = 0
    max_num = 3

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'rg', 'profissao')
    search_fields = ('nome', 'cpf', 'rg')
    inlines = [RendimentoInline]

admin.site.register(Rendimento)
