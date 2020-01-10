from django import forms

from exemplo.models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        # fields = ('nome', 'telefone')
        # exclude = ('celular', 'email')
