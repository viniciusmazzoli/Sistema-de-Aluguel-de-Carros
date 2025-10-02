# perfis/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso! Bem-vindo.')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'perfis/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'perfis/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard_view(request):
    user = request.user
    if user.perfil.tipo == 'agente':
        # Agentes veem pedidos "Em análise" de todos os clientes
        pedidos_para_avaliar = Pedido.objects.filter(status='analise')
        context = {
            'pedidos': pedidos_para_avaliar
        }
        return render(request, 'perfis/dashboard_agente.html', context)
    else:
        # --- CORREÇÃO APLICADA AQUI ---
        # A query agora é direta e simples: filtre os pedidos onde o campo 'cliente'
        # (que agora é uma ForeignKey para User) é o próprio usuário logado.
        pedidos_cliente = Pedido.objects.filter(cliente=user)
        
        context = {
            'pedidos': pedidos_cliente
        }
        return render(request, 'perfis/dashboard_cliente.html', context)

