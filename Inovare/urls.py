from django.urls import path
from . import views 

urlpatterns = [
    # path('', views.login_view, name='login'),
    # path('inicioadmin/', views.inicio_admin, name='inicioadmin'),
    # path('inicioforn/', views.inicio_forn, name='inicioforn'),
    # path('cadastrarfunc/', views.cadastrar_func, name='cadastrarfunc'),
    # path('relatorios/', views.relatorios, name='relatorios')
    path('funcionarios/', views.funcionario_list, name='funcionario_list'),
    path('funcionarios/new/', views.funcionario_create, name='funcionario_create'),
    path('funcionarios/edit/<int:pk>/', views.funcionario_update, name='funcionario_update'),
    path('funcionarios/delete/<int:pk>/', views.funcionario_delete, name='funcionario_delete'),

    path('funcionarios/', views.funcionario_list, name='funcionario_list'),
    path('funcionarios/new/', views.funcionario_create, name='funcionario_create'),
    path('funcionarios/edit/<int:pk>/', views.funcionario_update, name='funcionario_update'),
    path('funcionarios/delete/<int:pk>/', views.funcionario_delete, name='funcionario_delete'),

    path('funcionarios/', views.funcionario_list, name='funcionario_list'),
    path('funcionarios/new/', views.funcionario_create, name='funcionario_create'),
    path('funcionarios/edit/<int:pk>/', views.funcionario_update, name='funcionario_update'),
    path('funcionarios/delete/<int:pk>/', views.funcionario_delete, name='funcionario_delete'),

    # path('relatorio',)
]
