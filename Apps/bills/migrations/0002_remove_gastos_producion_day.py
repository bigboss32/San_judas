# Generated by Django 4.2.6 on 2024-04-09 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gastos',
            name='producion_day',
        ),
    ]
