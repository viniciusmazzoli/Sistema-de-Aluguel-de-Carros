# pedidos/urls.py
from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    # As views de lista e criação foram movidas para o dashboard e o fluxo do cliente
    path('<int:pk>/avaliar/', views.avaliar_pedido_view, name='avaliar'),
    path('<int:pk>/cancelar/', views.cancelar_pedido_view, name='cancelar'),
    path('novo/', views.PedidoCreateView.as_view(), name='criar'),
]
