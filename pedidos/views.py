# pedidos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Pedido, Contrato
from datetime import date

# -------------------------------------------------------------------
# View para um CLIENTE criar um novo pedido de aluguel.
# -------------------------------------------------------------------
class PedidoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pedido
    template_name = 'pedidos/pedido_form.html'
    fields = ['automovel']
    success_url = reverse_lazy('dashboard')
    success_message = "Pedido de aluguel criado com sucesso! Acompanhe o status pelo seu dashboard."

    # =======================================================
    # >> AQUI ESTÁ A CORREÇÃO FINAL E SIMPLIFICADA <<
    # =======================================================
    def form_valid(self, form):
        """
        Este método é chamado quando o formulário é válido.
        Nós o usamos para definir o 'cliente' do pedido como o usuário logado
        ANTES de salvar o objeto no banco de dados.
        """
        # Atribui o usuário logado ao campo 'cliente' do objeto que está sendo criado.
        form.instance.cliente = self.request.user
        # Agora, o fluxo normal do 'super().form_valid()' vai salvar o formulário
        # já com o campo 'cliente' preenchido corretamente.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Fazer um Novo Pedido de Aluguel'
        return context

# -------------------------------------------------------------------
# View para um AGENTE avaliar um pedido (Aprovar ou Reprovar).
# -------------------------------------------------------------------
@login_required
def avaliar_pedido_view(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    
    if not request.user.is_staff or request.user.perfil.tipo != 'agente':
        messages.error(request, 'Acesso negado. Apenas agentes podem avaliar pedidos.')
        return redirect('dashboard')

    if request.method == 'POST':
        status = request.POST.get('status')
        parecer = request.POST.get('parecer', '')

        if status in ['aprovado', 'reprovado']:
            pedido.status = status
            pedido.parecer_agente = parecer
            pedido.data_aprovacao = date.today()
            pedido.save()

            if status == 'aprovado':
                Contrato.objects.create(
                    pedido=pedido,
                    data_inicio=date.today(),
                    data_fim=date.today().replace(year=date.today().year + 1),
                    valor_total=5000.00
                )
                messages.success(request, f'Pedido #{pedido.id} foi APROVADO e o contrato foi gerado.')
            else:
                messages.warning(request, f'Pedido #{pedido.id} foi REPROVADO.')
            
            return redirect('dashboard')

    return render(request, 'pedidos/avaliar_pedido.html', {'pedido': pedido})

# -------------------------------------------------------------------
# View para um CLIENTE cancelar seu próprio pedido.
# -------------------------------------------------------------------
@login_required
def cancelar_pedido_view(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)

    if pedido.cliente != request.user:
        messages.error(request, 'Você não pode cancelar um pedido que não é seu.')
        return redirect('dashboard')
    
    if pedido.status == 'analise':
        pedido.status = 'cancelado'
        pedido.save()
        messages.info(request, f'Pedido #{pedido.id} foi cancelado com sucesso.')
    else:
        messages.error(request, 'Este pedido não pode mais ser cancelado, pois já foi avaliado.')

    return redirect('dashboard')
