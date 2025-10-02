# automoveis/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Automovel
from django.contrib.messages.views import SuccessMessageMixin

class AutomovelListView(ListView):
    model = Automovel
    template_name = 'automoveis/automovel_list.html'
    context_object_name = 'automoveis'
    paginate_by = 10

class AutomovelDetailView(DetailView):
    model = Automovel
    template_name = 'automoveis/automovel_detail.html'
    context_object_name = 'automovel'

class AutomovelCreateView(SuccessMessageMixin, CreateView):
    model = Automovel
    template_name = 'automoveis/automovel_form.html'
    fields = ['placa', 'marca', 'modelo', 'ano', 'matricula', 'content_type', 'object_id']
    success_url = reverse_lazy('automoveis:listar')
    success_message = "Automóvel cadastrado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo Automóvel'
        return context

class AutomovelUpdateView(SuccessMessageMixin, UpdateView):
    model = Automovel
    template_name = 'automoveis/automovel_form.html'
    fields = ['placa', 'marca', 'modelo', 'ano', 'matricula', 'content_type', 'object_id']
    success_url = reverse_lazy('automoveis:listar')
    success_message = "Automóvel atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Editar Automóvel: {self.object.placa}'
        return context

class AutomovelDeleteView(SuccessMessageMixin, DeleteView):
    model = Automovel
    template_name = 'automoveis/automovel_confirm_delete.html'
    success_url = reverse_lazy('automoveis:listar')
    success_message = "Automóvel removido com sucesso!"
