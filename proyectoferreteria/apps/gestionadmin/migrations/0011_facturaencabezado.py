# Generated by Django 2.2.6 on 2020-03-06 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0010_facturadetalle_idproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaEncabezado',
            fields=[
                ('idFacturaEncabezado', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nSar', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('codigoCAI', models.CharField(max_length=35)),
                ('isv18', models.IntegerField()),
                ('isv15', models.IntegerField()),
                ('totalFactura', models.IntegerField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Cliente')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.Empleado')),
                ('idFacturaDetalle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.FacturaDetalle')),
                ('idFormaPago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.FormaPago')),
                ('idMetodoPago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionadmin.MetodoPago')),
            ],
        ),
    ]
