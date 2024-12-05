from django.test import TestCase
from datetime import datetime
from django.utils import timezone
from .models import Funcionario_2, Fornecedor_2, Produtos_2


class TestDatabaseIntegration(TestCase):
    def setUp(self):
        # Configuração inicial de objetos
        self.fornecedor = Fornecedor_2.objects.create(
            nome_fornecedor="Fornecedor Teste",
            cnpj="12.345.678/0001-99",
            telefone="(11) 99999-9999",
            endereco="Rua Teste, 123"
        )

    def test_create_fornecedor(self):
        novo_fornecedor = Fornecedor_2.objects.create(
            nome_fornecedor="Novo Fornecedor",
            cnpj="98.765.432/0001-88",
            telefone="(21) 98888-8888",
            endereco="Avenida Exemplo, 456"
        )
        self.assertEqual(Fornecedor_2.objects.count(), 2)  # Já existe 1 criado no setUp
        self.assertEqual(novo_fornecedor.nome_fornecedor, "Novo Fornecedor")
        self.assertEqual(novo_fornecedor.cnpj, "98.765.432/0001-88")
        self.assertEqual(novo_fornecedor.telefone, "(21) 98888-8888")
        self.assertEqual(novo_fornecedor.endereco, "Avenida Exemplo, 456")
        print("Fornecedor Teste criado com sucesso!")

    def test_create_funcionario(self):
        funcionario = Funcionario_2.objects.create(
            nome_funcionario="Funcionario Teste",
            numero="123456789",
            email="joao@teste.com",
            data_nascimento="1990-01-01",
            cpf="123.456.789-00",
            rg="12.345.678-9"
        )
        self.assertEqual(Funcionario_2.objects.count(), 1)
        self.assertEqual(funcionario.nome_funcionario, "Funcionario Teste")
        print("Funcionário Teste criado com sucesso!")

    def test_create_produto(self):
        # Usando o fuso horário do Django configurado
        validade_com_fuso = timezone.make_aware(datetime(2024, 12, 12))

        produto = Produtos_2.objects.create(
            nomeprod="Produto Teste",
            desc="Descrição de teste",
            cod_barra="123456789",
            quant=10,
            validade=validade_com_fuso,
            fornecedor=self.fornecedor
        )
        self.assertEqual(Produtos_2.objects.count(), 1)
        self.assertEqual(produto.fornecedor.nome_fornecedor, "Fornecedor Teste")
        print("Produto Teste criado com sucesso!")
