from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib import messages
from django.db.models import Q

from .models import Cliente
from .forms import ClienteForm, RendimentoFormSet

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(cpf__icontains=q))
        return qs

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'

def cliente_create(request):
    cliente = Cliente()
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        formset = RendimentoFormSet(request.POST, instance=cliente)
        if form.is_valid() and formset.is_valid():
            cliente = form.save()
            formset.instance = cliente
            # Validação: no máx. 3 rendimentos salvos efetivamente
            rendimentos_validos = [f for f in formset.forms if f.cleaned_data and not f.cleaned_data.get('DELETE', False)]
            if len(rendimentos_validos) > 3:
                messages.error(request, 'Máximo de 3 rendimentos permitidos.')
            else:
                formset.save()
                messages.success(request, 'Cliente criado com sucesso!')
                return redirect('clientes:listar')
    else:
        form = ClienteForm(instance=cliente)
        formset = RendimentoFormSet(instance=cliente)

    return render(request, 'clientes/cliente_form.html', {
        'form': form,
        'formset': formset,
        'titulo': 'Novo Cliente'
    })

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        formset = RendimentoFormSet(request.POST, instance=cliente)
        if form.is_valid() and formset.is_valid():
            cliente = form.save()
            formset.instance = cliente
            rendimentos_validos = [f for f in formset.forms if f.cleaned_data and not f.cleaned_data.get('DELETE', False)]
            if len(rendimentos_validos) > 3:
                messages.error(request, 'Máximo de 3 rendimentos permitidos.')
            else:
                formset.save()
                messages.success(request, 'Cliente atualizado com sucesso!')
                return redirect('clientes:listar')
    else:
        form = ClienteForm(instance=cliente)
        formset = RendimentoFormSet(instance=cliente)

    return render(request, 'clientes/cliente_form.html', {
        'form': form,
        'formset': formset,
        'titulo': f'Editar Cliente: {cliente.nome}'
    })

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes:listar')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Cliente removido com sucesso!')
        return super().delete(request, *args, **kwargs)
