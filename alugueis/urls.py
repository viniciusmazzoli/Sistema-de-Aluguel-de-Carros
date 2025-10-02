# alugueis/urls.py
from django.contrib import admin
from django.urls import path, include
from perfis.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # A raiz do site agora é a tela de login
    path('', login_view, name='home'), 
    
    # URLs de autenticação e dashboard
    path('contas/', include('perfis.urls')),

    # Mantemos as URLs dos outros apps, mas elas serão acessadas de outras formas
    path('automoveis/', include('automoveis.urls', namespace='automoveis')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
]
