from django.contrib import admin
from .models import Agente, Banco, Empresa

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'email_contato')
    list_filter = ('tipo',)
    search_fields = ('nome',)

admin.site.register(Banco)
admin.site.register(Empresa)
