# Generated by Django 4.2.6 on 2024-12-03 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar el catálogo de vehículos')]},
        ),
    ]