from django.db import models
import uuid


class Funcionario_2(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome_funcionario

    class Meta:
        verbose_name = "Funcionário_2"
        verbose_name_plural = "Funcionários_2"

class Fornecedor_2(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome_fornecedor = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20, unique=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_fornecedor

    class Meta:
        verbose_name = "Fornecedor_2"
        verbose_name_plural = "Fornecedores_2"

class Produtos_2(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nomeprod = models.CharField(max_length=100)
    desc = models.TextField()
    cod_barra = models.UUIDField(unique=True, default=uuid.uuid4)
    quant = models.IntegerField()
    validade = models.DateTimeField(blank=True)
    fornecedor = models.ForeignKey(Fornecedor_2, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeprod

    class Meta:
        verbose_name = "Produto_2"
        verbose_name_plural = "Produtos_2"

class Relatorio_2(models.Model):
    id_relatorio = models.AutoField(primary_key=True)
    data_relat = models.DateTimeField(auto_now_add=True)
    responsavel = models.ForeignKey(Funcionario_2, on_delete=models.CASCADE)
    resumo = models.TextField()
    total_itens = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    entrada = models.IntegerField()
    saida = models.IntegerField()
    analise_rapida = models.BooleanField(default=False)
    recomendacoes = models.TextField(blank=True)
    produto = models.ForeignKey(Produtos_2, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return f"Relatório {self.data_relat.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Relatório_2"
        verbose_name_plural = "Relatórios_2"
        ordering = ['-data_relat']
        