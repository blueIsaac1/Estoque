# Generated by Django 5.1.2 on 2024-11-19 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inovare', '0015_alter_relatorio_2_entrada_alter_relatorio_2_saida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.PositiveIntegerField()),
                ('resumo', models.TextField()),
                ('analise_rapida', models.BooleanField()),
                ('recomendacoes', models.TextField()),
                ('data_entrada', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inovare.produtos_2')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inovare.funcionario_2')),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.PositiveIntegerField()),
                ('resumo', models.TextField()),
                ('analise_rapida', models.BooleanField()),
                ('recomendacoes', models.TextField()),
                ('data_saida', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inovare.produtos_2')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inovare.funcionario_2')),
            ],
        ),
    ]