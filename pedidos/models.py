from django.db import models
from django.contrib.auth.models import User 
from automoveis.models import Automovel
from agentes.models import Banco

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('analise', 'Em análise'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
        ('cancelado', 'Cancelado'),
    )
    cliente = models.ForeignKey(User, on_delete=models.PROTECT, related_name='pedidos')
    automovel = models.ForeignKey(Automovel, on_delete=models.PROTECT, related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES, default='analise')
    parecer_agente = models.TextField('Parecer do Agente', blank=True)
    data_aprovacao = models.DateTimeField('Data de Aprovação/Reprovação', null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome} para {self.automovel.placa}"

    class Meta:
        verbose_name = 'Pedido de Aluguel'
        verbose_name_plural = 'Pedidos de Aluguel'
        ordering = ['-data_pedido']

class Contrato(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'status': 'aprovado'})
    banco_credor = models.ForeignKey(Banco, on_delete=models.SET_NULL, null=True, blank=True, help_text='Banco que concedeu o crédito, se aplicável.')
    data_inicio = models.DateField('Data de Início')
    data_fim = models.DateField('Data de Fim')
    valor_total = models.DecimalField('Valor Total (R$)', max_digits=12, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contrato para o Pedido #{self.pedido.id}"

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
