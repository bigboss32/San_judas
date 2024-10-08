# Generated by Django 4.2.6 on 2024-03-17 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_register', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, default='', null=True)),
                ('second_name', models.CharField(blank=True, default='', null=True)),
                ('last_name', models.CharField(blank=True, default='', null=True)),
                ('second_last_name', models.CharField(blank=True, default='', null=True)),
                ('cedula', models.IntegerField(blank=True, null=True)),
                ('celular', models.BigIntegerField(blank=True, null=True)),
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
                ('liter', models.IntegerField(blank=True, null=True)),
                ('value_liter', models.IntegerField(blank=True, null=True)),
                ('adelantos', models.IntegerField(default=0)),
                ('producionday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.producionday')),
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
