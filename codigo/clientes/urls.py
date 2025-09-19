from django.urls import path
from .views import (
    ClienteListView, ClienteDetailView,
    cliente_create, cliente_update, ClienteDeleteView
)

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='listar'),
    path('novo/', cliente_create, name='criar'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='detalhar'),
    path('<int:pk>/editar/', cliente_update, name='editar'),
    path('<int:pk>/excluir/', ClienteDeleteView.as_view(), name='excluir'),
]
