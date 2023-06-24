# Generated by Django 4.2.2 on 2023-06-24 00:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_eliminacion_ubicacion_tabla_imagenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='producto'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
