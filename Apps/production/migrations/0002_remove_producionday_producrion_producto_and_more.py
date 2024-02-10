# Generated by Django 4.2.6 on 2024-01-14 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producionday',
            name='producrion_producto',
        ),
        migrations.RemoveField(
            model_name='productionproducto',
            name='register_day',
        ),
        migrations.AddField(
            model_name='productionproducto',
            name='producionday',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='production.producionday'),
            preserve_default=False,
        ),
    ]