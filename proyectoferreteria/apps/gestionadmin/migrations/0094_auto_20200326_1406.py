# Generated by Django 3.0.4 on 2020-03-26 20:06

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0093_auto_20200326_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaencabezado',
            name='ISV15',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos]),
        ),
        migrations.AlterField(
            model_name='facturaencabezado',
            name='ISV18',
            field=models.IntegerField(validators=[proyectoferreteria.apps.gestionadmin.models.validarnegativos]),
        ),
    ]
