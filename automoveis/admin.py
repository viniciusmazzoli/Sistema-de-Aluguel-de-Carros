from django.contrib import admin
from .models import Automovel

@admin.register(Automovel)
class AutomovelAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'ano', 'proprietario')
    search_fields = ('placa', 'marca', 'modelo')
    list_filter = ('marca', 'ano')
