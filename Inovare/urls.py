from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('inicioadmin/', views.inicio_admin, name='inicioadmin'),
    path('inicioforn/', views.inicio_forn, name='inicioforn'),
    path('cadastrarfunc/', views.cadastrar_func, name='cadastrarfunc'),
    path('cadastroproduto/', views.cadastro_produto, name='cadastroproduto'),
    path('cadastroforn/', views.cadastro_forn, name='cadastroforn'),
    path('editar/', views.editar, name='editar'),
    path('movimentacoes/', views.movimentacao, name='movimentacoes'),
    path('relatorios/', views.relatorio_movimentacoes, name='relatorio_movimentacoes'),
    path('entradaprod/', views.registrar_entrada, name='entradaprod'),
    path('saidaprod/', views.registrar_saida, name='saidaprod'),
    path('galeria/', views.galeria, name='galeria'),

    
    path('editar_fornecedor/<int:id_fornecedor>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('listar_fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('deletar_fornecedor/<int:id_fornecedor>/', views.deletar_fornecedor, name='deletar_fornecedor'),

    
    path('editar_funcionario/<int:id_funcionario>/', views.editar_funcionario, name='editar_funcionario'),
    path('listar_funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('deletar_funcionario/<int:id_funcionario>/', views.deletar_funcionario, name='deletar_funcionario'),

    
    path('editar_produto/<int:id_produto>/', views.editar_produto, name='editar_produto'),
    path('listar_produto/', views.listar_produtos, name='listar_produto'),
    path('deletar_produto/<int:id_produto>/', views.deletar_produto, name='deletar_produto'),
]

#Define as URLs da sua aplicação Django