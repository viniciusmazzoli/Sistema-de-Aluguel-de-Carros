from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=120)
    rg = models.CharField('RG', max_length=20, unique=True,
                          validators=[RegexValidator(r'^[0-9.\-A-Za-z]+$')])
    cpf = models.CharField('CPF', max_length=14, unique=True,
                           help_text='Formato: 000.000.000-00',
                           validators=[RegexValidator(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')])
    endereco = models.CharField('Endereço', max_length=200)
    profissao = models.CharField('Profissão', max_length=80, blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome} ({self.cpf})'


class Rendimento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='rendimentos')
    empregador = models.CharField('Entidade Empregadora', max_length=120)
    valor = models.DecimalField('Valor (R$)', max_digits=12, decimal_places=2,
                                validators=[MinValueValidator(0)])
    observacao = models.CharField('Observação', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Rendimento'
        verbose_name_plural = 'Rendimentos'

    def __str__(self):
        return f'{self.empregador} - R${self.valor}'
