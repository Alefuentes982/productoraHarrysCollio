# Generated by Django 5.0.3 on 2024-07-13 02:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes_proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('recargo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios_categorias.categoria')),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios_categorias.extra')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicios_categorias_proveedores', to='clientes_proveedores.proveedor')),
            ],
        ),
    ]