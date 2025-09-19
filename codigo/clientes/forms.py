from django import forms
from django.forms import inlineformset_factory
from .models import Cliente, Rendimento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'rg', 'cpf', 'endereco', 'profissao']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'rg': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder':'000.000.000-00'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'profissao': forms.TextInput(attrs={'class':'form-control'}),
        }

class RendimentoForm(forms.ModelForm):
    class Meta:
        model = Rendimento
        fields = ['empregador', 'valor', 'observacao']
        widgets = {
            'empregador': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.NumberInput(attrs={'class':'form-control', 'step':'0.01', 'min':'0'}),
            'observacao': forms.TextInput(attrs={'class':'form-control'}),
        }

RendimentoFormSet = inlineformset_factory(
    Cliente, Rendimento,
    form=RendimentoForm,
    fields=['empregador', 'valor', 'observacao'],
    extra=3, max_num=3, can_delete=True, validate_max=True
)
