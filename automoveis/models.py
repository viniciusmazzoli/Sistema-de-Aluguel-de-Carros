# automoveis/models.py

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator

class Automovel(models.Model):
    # Validador para placa (padrão antigo e Mercosul)
    placa_validator = RegexValidator(
        regex=r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$',
        message='A placa deve estar no formato AAA1234 ou AAA1B34 (padrão Mercosul).'
    )

    placa = models.CharField(
        'Placa',
        max_length=7,
        unique=True,
        validators=[placa_validator],
        help_text='Formato AAA1234 ou AAA1B34'
    )
    
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    ano = models.PositiveIntegerField('Ano')
    matricula = models.CharField('Matrícula', max_length=50, unique=True)

    # =======================================================
    # >> AQUI ESTÁ A CORREÇÃO <<
    # =======================================================
    # O proprietário agora pode ser um 'Perfil' (que representa um cliente) ou um 'Agente'.
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=models.Q(app_label='perfis', model='perfil') | # MUDOU DE 'clientes' PARA 'perfis'
                         models.Q(app_label='agentes', model='agente'),
        verbose_name='Tipo de Proprietário'
    )
    object_id = models.PositiveIntegerField('ID do Proprietário')
    proprietario = GenericForeignKey('content_type', 'object_id')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

    class Meta:
        verbose_name = 'Automóvel'
        verbose_name_plural = 'Automóveis'
        ordering = ['marca', 'modelo']
