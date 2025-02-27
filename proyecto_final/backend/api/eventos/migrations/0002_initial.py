# Generated by Django 5.0.3 on 2024-07-13 02:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0001_initial'),
        ('servicios_categorias', '0001_initial'),
        ('ventas_cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas_cotizaciones.estadocot'),
        ),
        migrations.AddField(
            model_name='evento',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios_categorias.servicio'),
        ),
    ]
