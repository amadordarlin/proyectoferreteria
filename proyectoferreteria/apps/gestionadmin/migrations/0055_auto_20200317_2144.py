# Generated by Django 2.2.6 on 2020-03-18 03:44

from django.db import migrations, models
import proyectoferreteria.apps.gestionadmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0054_auto_20200317_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnoempleado',
            name='Turno',
            field=models.CharField(default=234, max_length=30, validators=[proyectoferreteria.apps.gestionadmin.models.validarnombre]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marca',
            name='idMarca',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[proyectoferreteria.apps.gestionadmin.models.validartamaño]),
        ),
    ]
