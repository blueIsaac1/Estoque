# Generated by Django 5.1.1 on 2024-10-17 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inovare', '0002_relatorio_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatorio',
            name='analise_rapida',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='codigo_barra',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='custo_unidade',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='estoque',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='notas',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='preco',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='quantidade',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='recomendacoes',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='saida',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='total',
        ),
        migrations.CreateModel(
            name='ItemRelatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('codigo_barra', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('custo_unidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('relatorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='Inovare.relatorio')),
            ],
        ),
    ]
