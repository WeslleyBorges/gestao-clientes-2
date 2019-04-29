# Generated by Django 2.2 on 2019-04-12 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20190411_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Parâmetro para definir se o usuário está apto a algo relacionado a NF-e'), ('Permissão Dois', 'A segunda permissão para algo'), ('Permissão Três', 'A terceira permissão para algo'))},
        ),
        migrations.RemoveField(
            model_name='venda',
            name='valor_total',
        ),
    ]