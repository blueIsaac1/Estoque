from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Funcionario_2, Fornecedor_2, Produtos_2, Relatorio_2
from .forms import FuncionarioForm, FornecedorForm, ProdutosForm, RelatorioForm
from django.contrib.auth import authenticate, login
import uuid

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_staff:
            login(request, user)
            return redirect('inicio_admin')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def relatorios(request):
    return render(request, 'relatorio.html') 


def inicio_admin(request):
    return render(request, 'inicioadmin.html')


def inicio_forn(request):
    return render(request, '/inicioforn.html')
# codigo de barra: codgbrra = uuid.uuid4().hex[:10]

# CRUD Funcionario
def funcionario_list(request):
    funcionarios = Funcionario_2.objects.all()
    return render(request, 'funcionario_list.html', {'funcionarios': funcionarios})

def funcionario_create(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm()
    return render(request, 'funcionario_form.html', {'form': form})

def funcionario_update(request, pk):
    funcionario = get_object_or_404(Funcionario_2, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionario_form.html', {'form': form})

def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario_2, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('funcionario_list')
    return render(request, 'funcionario_confirm_delete.html', {'funcionario': funcionario})

# CRUD Fornecedores

def fornecedores_list(request):
    fornecedores = Fornecedor_2.objects.all()
    return render(request, 'fornecedores_list.html', {'fornecedores': fornecedores})

def fornecedores_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores_list')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedor_form.html', {'form': form})

def fornecedor_update(request, pk):
    fornecedor = get_object_or_404(Fornecedor_2, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('Fornecedor_list')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedor_form.html', {'form': form})

def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedor_2, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedor_list')
    return render(request, 'fornecedor_confirm_delete.html', {'fornecedor': fornecedor})


# CRUD Produtos


def produtos_list(request):
    produtos = Produtos_2.objects.all()
    return render(request, 'produtos_list.html', {'produtos': produtos})

def produtos_create(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos_list')
    else:
        form = ProdutosForm()
    return render(request, 'produtos_form.html', {'form': form})

def produtos_update(request, pk):
    produtos = get_object_or_404(Produtos_2, pk=pk)
    if request.method == 'POST':
        form = ProdutosForm(request.POST, instance=produtos)
        if form.is_valid():
            form.save()
            return redirect('produtos_list')
    else:
        form = ProdutosForm(instance=produtos)
    return render(request, 'produtos_form.html', {'form': form})

def produtos_delete(request, pk):
    produtos = get_object_or_404(Produtos_2, pk=pk)
    if request.method == 'POST':
        produtos.delete()
        return redirect('produto_list')
    return render(request, 'produto_confirm_delete.html', {'produtos': produtos})


    
