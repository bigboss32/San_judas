# Generated by Django 4.2.6 on 2024-01-21 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("liter_control", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="registerday",
            old_name="chofer",
            new_name="trasporte",
        ),
    ]
