from django import forms
from .models import Funcionario_2, Fornecedor_2, Produtos_2, Relatorio_2

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario_2
        fields = ['nome_funcionario', 'numero', 'email', 'data_nascimento', 'cpf', 'rg']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor_2
        fields = ['nome_fornecedor', 'cnpj', 'telefone', 'endereco']

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos_2
        fields = ['nomeprod', 'desc', 'cod_barra', 'quant', 'validade']

class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio_2
        fields = ['responsavel', 'resumo', 'total_itens', 'valor_total', 'entrada', 'saida', 'analise_rapida', 'recomendacoes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsavel'].queryset = Funcionario_2.objects.all()