from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Funcionario_2, Fornecedor_2, Produtos_2, Relatorio_2
from .forms import FuncionarioForm, FornecedorForm, ProdutosForm, RelatorioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
import uuid
import logging

logger = logging.getLogger(__name__)

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('inicio_admin')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            logger.warning("Tentativa de login falhou para o usuário: %s", username)
    return render(request, 'login.html')

# Relatórios View
def relatorios(request):
    logger.info("Iniciando o relatório.")
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Relatório cadastrado com sucesso!")
                logger.info("Relatório salvo com sucesso.")
                return redirect('inicioadmin')
            except Exception as e:
                messages.error(request, "Erro ao cadastrar Relatório.")
                logger.error(f"Erro ao salvar relatório: {e}")
        else:
            messages.warning(request, "Formulário inválido. Verifique os campos.")
            logger.warning("Formulário inválido. Erros: %s", form.errors)
    else:
        form = RelatorioForm()
        logger.info("Requisição GET recebida, exibindo formulário vazio.")
    return render(request, 'relatorio.html', {'form': form})

# Main View
def main(request):
    return render(request, 'login.html')

# Admin Home View
def inicio_admin(request):
    return render(request, 'inicioadmin.html')

# Fornecedor Home View
def inicio_forn(request):
    return render(request, 'inicioforn.html')

# Editar View
def editar(request):
    return render(request, 'editar.html')

# Movimentações View
def movimentacao(request):
    return render(request, 'movimentacoes.html')

# Cadastrar Funcionário
def cadastrar_func(request):
    logger.info("Iniciando o cadastro de funcionário.")
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Funcionário cadastrado com sucesso!")
                logger.info("Funcionário salvo com sucesso.")
                return redirect('inicioadmin')
            except Exception as e:
                messages.error(request, "Erro ao cadastrar funcionário.")
                logger.error(f"Erro ao salvar funcionário: {e}")
        else:
            messages.warning(request, "Formulário inválido. Verifique os campos.")
            logger.warning("Formulário inválido. Erros: %s", form.errors)
    else:
        form = FuncionarioForm()
        logger.info("Requisição GET recebida, exibindo formulário vazio.")
    return render(request, 'cadastrofunc.html', {'form': form})

# Cadastrar Fornecedor
def cadastro_forn(request):
    logger.info("Iniciando o cadastro de fornecedor.")
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Fornecedor cadastrado com sucesso!")
                logger.info("Fornecedor salvo com sucesso.")
                return redirect('inicioadmin')
            except Exception as e:
                messages.error(request, "Erro ao cadastrar fornecedor.")
                logger.error(f"Erro ao salvar fornecedor: {e}")
        else:
            messages.warning(request, "Formulário inválido. Verifique os campos.")
            logger.warning("Formulário inválido. Erros: %s", form.errors)
    else:
        form = FornecedorForm()
        logger.info("Requisição GET recebida, exibindo formulário vazio.")
    return render(request, 'cadastroforn.html', {'form': form})

# Cadastrar Produto
def cadastro_produto(request):
    logger.info("Iniciando o cadastro de produto .")
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            try:
                produto = form.save(commit=False)
                produto.cod_barra = uuid.uuid4()
                produto.save()
                messages.success(request, "Produto cadastrado com sucesso!")
                logger.info("Produto salvo com sucesso.")
                return redirect('inicioadmin')
            except Exception as e:
                messages.error(request, "Erro ao cadastrar produto.")
                logger.error(f"Erro ao salvar produto: {e}")
        else:
            messages.warning(request, "Formulário inválido. Verifique os campos.")
            logger.warning("Formulário inválido. Erros: %s", form.errors)
    else:
        form = ProdutosForm()
        logger.info("Requisição GET recebida, exibindo formulário vazio.")
    return render(request, 'cadastro_produto.html', {'form': form})

# Registrar Entrada de Produto
def registrar_entrada(request):
    logger.info("Iniciando a movimentação de produtos.")
    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        entrada = int(request.POST.get('entrada', 0))
        responsavel_id = request.POST.get('responsavel')
        resumo = request.POST.get('resumo')
        total_itens = int(request.POST.get('total_itens', 0))
        valor_total = float(request.POST.get('valor_total', 0))
        analise_rapida = request.POST.get('analise_rapida')
        recomendacoes = request.POST.get('recomendacoes')

        try:
            produto = Produtos_2.objects.get(id_produto=produto_id)
            responsavel = Funcionario_2.objects.get(id_funcionario=responsavel_id)
        except (Produtos_2.DoesNotExist, Funcionario_2.DoesNotExist) as e:
            logger.error("Produto ou responsável não encontrados: %s", e)
            messages.error(request, "Produto ou responsável não encontrados.")
            return redirect('movimentacao_produto')


        produto.quant += entrada
        produto.save()

        Relatorio_2.objects.create(
            produto=produto,
            entrada=entrada,
            responsavel=responsavel,
            resumo=resumo,
            total_itens=total_itens,
            valor_total=valor_total,
            analise_rapida=analise_rapida,
            recomendacoes=recomendacoes,
        )

        messages.success(request, "Movimentação registrada com sucesso!")
        logger.info("Movimentação registrada com sucesso.")
        return redirect('relatorio_movimentacoes')

    else:
        produtos = Produtos_2.objects.all()
        funcionarios = Funcionario_2.objects.all()
        logger.info("Requisição GET recebida, exibindo formulário vazio.")
        return render(request, 'entradaprod.html', {
            'produtos': produtos,
            'funcionarios': funcionarios
        })


# Registrar Saída de Produto
def registrar_saida(request):
    logger.info("Iniciando a movimentação de produtos.")
    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        saida = int(request.POST.get('saida', 0))
        responsavel_id = request.POST.get('responsavel')
        resumo = request.POST.get('resumo')
        total_itens = int(request.POST.get('total_itens', 0))
        valor_total = float(request.POST.get('valor_total', 0))
        analise_rapida = request.POST.get('analise_rapida')
        recomendacoes = request.POST.get('recomendacoes')

        try:
            produto = Produtos_2.objects.get(id_produto=produto_id)
            responsavel = Funcionario_2.objects.get(id_funcionario=responsavel_id)
        except (Produtos_2.DoesNotExist, Funcionario_2.DoesNotExist) as e:
            logger.error("Produto ou responsável não encontrados: %s", e)
            messages.error(request, "Produto ou responsável não encontrados.")
            return redirect('movimentacao_produto')

        produto.quant -= saida
        produto.save()

        Relatorio_2.objects.create(
            produto=produto,
            saida=saida,
            responsavel=responsavel,
            resumo=resumo,
            total_itens=total_itens,
            valor_total=valor_total,
            analise_rapida=analise_rapida,
            recomendacoes=recomendacoes,
        )

        messages.success(request, "Movimentação registrada com sucesso!")
        logger.info("Movimentação registrada com sucesso.")
        return redirect('relatorio_movimentacoes')

    else:
        produtos = Produtos_2.objects.all()
        funcionarios = Funcionario_2.objects.all()
        logger.info("Requisição GET recebida, exibindo formulário vazio.")
        return render(request, 'saidaprod.html', {
            'produtos': produtos,
            'funcionarios': funcionarios
        })

# Relatório de Movimentações
def relatorio_movimentacoes(request):
    movimentacoes = Relatorio_2.objects.select_related('responsavel', 'produto').all()
    filtro_entrada = Relatorio_2.objects.filter(entrada__gte=0)
    filtro_saida = Relatorio_2.objects.filter(saida__gte=0)
    print(filtro_entrada)
    print(filtro_saida)
    return render(request, 'relatorio.html', {
        'movimentacoes': movimentacoes,
        'filtro_entrada': filtro_entrada,
        'filtro_saida': filtro_saida
    })

def entrada_saida(request):
    filtro_entrada = Relatorio_2.objects.filter(entrada__gte=0)
    filtro_saida = Relatorio_2.objects.filter(saida__gte=0)
    return render(request, 'entrada_saida.html', {
        'filtro_entrada': filtro_entrada,
        'filtro_saida': filtro_saida
    })

# Editar Fornecedor
def editar_fornecedor(request, id_fornecedor):
    fornecedor = get_object_or_404(Fornecedor_2, id_fornecedor=id_fornecedor)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            messages.success(request, "Fornecedor editado com sucesso!")
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'editarforn.html', {'form': form, 'fornecedor': fornecedor})

# Listar Fornecedores
def listar_fornecedores(request):
    fornecedores = Fornecedor_2.objects.all()
    return render(request, 'listar_forn.html', {'fornecedores': fornecedores})

# Deletar Fornecedor
def deletar_fornecedor(request, id_fornecedor):
    fornecedor = get_object_or_404(Fornecedor_2, id_fornecedor=id_fornecedor)
    if request.method == 'POST':
        fornecedor.delete()
        messages.success(request, "Fornecedor deletado com sucesso!")
        return redirect('listar_fornecedores')
    return render(request, 'deletar_forn.html', {'fornecedor': fornecedor})

# Editar Funcionário
def editar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(Funcionario_2, id_funcionario=id_funcionario)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário editado com sucesso!")
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'editarfunc.html', {'form': form, 'funcionario': funcionario})

# Listar Funcionários
def listar_funcionarios(request):
    funcionarios = Funcionario_2.objects.all()
    return render(request, 'listar_func.html', {'funcionarios': funcionarios})

# Deletar Funcionário
def deletar_funcionario(request, id_funcionario):
    funcionario = get_object_or_404(Funcionario_2, id_funcionario=id_funcionario)
    if request.method == 'POST':
        funcionario.delete()
        messages.success(request, "Funcionário deletado com sucesso!")
        return redirect('listar_funcionarios')
    return render(request, 'deletar_func.html', {'funcionario': funcionario})

# Editar Produto
def editar_produto(request, id_produto):
    produto = get_object_or_404(Produtos_2, id_produto=id_produto)
    if request.method == 'POST':
        form = ProdutosForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto editado com sucesso!")
            return redirect('listar_produto')
    else:
        form = ProdutosForm(instance=produto)
    return render(request, 'editarprod.html', {'form': form, 'produto': produto})

# Listar Produtos
def listar_produtos(request):
    produtos = Produtos_2.objects.all()
    return render(request, 'listar_prod.html', {'produtos': produtos})

# Deletar Produto
def deletar_produto(request, id_produto):
    produto = get_object_or_404(Produtos_2, id_produto=id_produto)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, "Produto deletado com sucesso!")
        return redirect('listar_produto')
    return render(request, 'deletar_prod.html', {'produto': produto})

#São funções responsáveis por processar as requisições do usuário e retornar as respostas,
#como renderizar templates ou manipular dados no banco de dados.