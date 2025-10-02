# perfis/admin.py

from django.contrib import admin
from .models import Perfil # Importe o modelo Perfil

# Crie uma classe para customizar como o Perfil é exibido
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo') # Colunas que aparecerão na lista
    list_filter = ('tipo',) # Adiciona um filtro por tipo de usuário
    search_fields = ('user__username',) # Permite buscar pelo nome do usuário

# Registre o modelo Perfil com a sua classe customizada
admin.site.register(Perfil, PerfilAdmin)
