# Generated by Django 5.0.3 on 2024-07-13 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios_categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='extra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios_categorias.extra'),
        ),
    ]