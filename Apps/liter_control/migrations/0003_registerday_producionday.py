# Generated by Django 4.2.6 on 2024-01-21 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_remove_producionday_register_day_producionday_day'),
        ('liter_control', '0002_rename_chofer_registerday_trasporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerday',
            name='producionday',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='production.producionday'),
            preserve_default=False,
        ),
    ]