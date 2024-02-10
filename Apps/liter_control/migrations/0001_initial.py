# Generated by Django 4.2.6 on 2024-01-14 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transportation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_register', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField()),
                ('second_name', models.CharField()),
                ('last_name', models.CharField()),
                ('second_last_name', models.CharField()),
                ('cedula', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_register', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('name_route', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='RegisterDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_register', models.DateTimeField(auto_now_add=True)),
                ('day', models.DateField(blank=True, default=None, null=True)),
                ('liter', models.IntegerField()),
                ('value_liter', models.IntegerField()),
                ('adelantos', models.IntegerField(default=0)),
                ('value_total', models.IntegerField(blank=True, null=True)),
                ('value_total_adelantos', models.IntegerField(blank=True, null=True)),
                ('chofer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation.trasporte')),
                ('provedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='liter_control.provedor')),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='liter_control.ruta')),
            ],
        ),
        migrations.AddField(
            model_name='provedor',
            name='ruta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='liter_control.ruta'),
        ),
    ]
