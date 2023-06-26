# Generated by Django 4.2.1 on 2023-06-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosEscultura',
            fields=[
                ('dies', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Dies')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripcion')),
                ('precio', models.IntegerField(blank=True, verbose_name='Precio')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='ProductosLana',
            fields=[
                ('dila', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Dila')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripcion')),
                ('precio', models.IntegerField(blank=True, verbose_name='Precio')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='ProductosLienzo',
            fields=[
                ('dili', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Dili')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripcion')),
                ('precio', models.IntegerField(blank=True, verbose_name='Precio')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
            ],
        ),
    ]