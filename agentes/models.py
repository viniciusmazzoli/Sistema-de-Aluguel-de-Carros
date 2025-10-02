from django.db import models

class Agente(models.Model):
    TIPO_CHOICES = (
        ('banco', 'Banco'),
        ('empresa', 'Empresa'),
    )
    nome = models.CharField('Nome', max_length=150)
    tipo = models.CharField('Tipo', max_length=10, choices=TIPO_CHOICES)
    email_contato = models.EmailField('Email de Contato')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        ordering = ['nome']

class Banco(models.Model):
    agente = models.OneToOneField(Agente, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'tipo': 'banco'})
    codigo_bancario = models.CharField('Código Bancário', max_length=10, unique=True)

    def __str__(self):
        return self.agente.nome

class Empresa(models.Model):
    agente = models.OneToOneField(Agente, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'tipo': 'empresa'})
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)

    def __str__(self):
        return self.agente.nome
