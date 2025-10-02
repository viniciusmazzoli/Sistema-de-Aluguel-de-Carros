# perfis/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    TIPO_USUARIO_CHOICES = (
        ('cliente', 'Cliente'),
        ('agente', 'Agente'),
    )
    
    # Relação 1-para-1 com o modelo User do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Nossos campos adicionais
    tipo = models.CharField('Tipo de Usuário', max_length=10, choices=TIPO_USUARIO_CHOICES, default='cliente')
    cpf = models.CharField('CPF', max_length=14, unique=True, null=True, blank=True)
    rg = models.CharField('RG', max_length=20, unique=True, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=200, blank=True)
    profissao = models.CharField('Profissão', max_length=80, blank=True)

    def __str__(self):
        return self.user.username

# Esta função cria um Perfil automaticamente toda vez que um User é criado.
@receiver(post_save, sender=User)
def criar_ou_atualizar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()
