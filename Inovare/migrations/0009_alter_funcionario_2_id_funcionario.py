# Generated by Django 5.1.1 on 2024-10-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inovare', '0008_rename_fornecedor_fornecedor_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario_2',
            name='id_funcionario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
