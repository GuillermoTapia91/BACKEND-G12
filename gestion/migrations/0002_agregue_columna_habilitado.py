# Generated by Django 4.2.2 on 2023-06-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_creacion_tablas'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
