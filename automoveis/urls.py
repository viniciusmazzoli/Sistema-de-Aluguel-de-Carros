# automoveis/urls.py

from django.urls import path
from . import views

app_name = 'automoveis'

urlpatterns = [
    path('', views.AutomovelListView.as_view(), name='listar'),
    path('novo/', views.AutomovelCreateView.as_view(), name='criar'),
    path('<int:pk>/', views.AutomovelDetailView.as_view(), name='detalhar'),
    path('<int:pk>/editar/', views.AutomovelUpdateView.as_view(), name='editar'),
    path('<int:pk>/excluir/', views.AutomovelDeleteView.as_view(), name='excluir'),
]
