# Generated by Django 2.2.6 on 2020-04-08 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0099_auto_20200402_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturaencabezado',
            old_name='Necha',
            new_name='Fecha',
        ),
        migrations.AddField(
            model_name='facturaencabezado',
            name='Id_producto',
            field=models.ManyToManyField(to='gestionadmin.Producto'),
        ),
    ]