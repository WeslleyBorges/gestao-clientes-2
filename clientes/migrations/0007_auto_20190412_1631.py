# Generated by Django 2.2 on 2019-04-12 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20190410_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'permissions': (('visualizar_pessoa_detail', 'Permissão para visualizar as informações de uma pessoa específica.'),)},
        ),
    ]