# Generated by Django 2.2.6 on 2020-03-16 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0036_auto_20200315_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precioCompra',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precioVenta',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
