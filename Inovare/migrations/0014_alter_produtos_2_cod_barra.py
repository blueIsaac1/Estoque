# Generated by Django 5.1.1 on 2024-11-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inovare', '0013_relatorio_2_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos_2',
            name='cod_barra',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]