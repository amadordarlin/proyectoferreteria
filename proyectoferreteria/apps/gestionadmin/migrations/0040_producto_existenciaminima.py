# Generated by Django 2.2.6 on 2020-03-16 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0039_auto_20200315_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='existenciaMinima',
            field=models.IntegerField(default=567),
            preserve_default=False,
        ),
    ]
