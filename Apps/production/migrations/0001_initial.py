# Generated by Django 4.2.6 on 2024-01-14 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("liter_control", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductionProducto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("producto", models.CharField(blank=True, null=True)),
                (
                    "register_day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="liter_control.registerday",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProducionDay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_register", models.DateTimeField(auto_now_add=True)),
                ("name_producction", models.CharField(blank=True, null=True)),
                (
                    "producrion_producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="production.productionproducto",
                    ),
                ),
                (
                    "register_day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="liter_control.registerday",
                    ),
                ),
            ],
            options={
                "unique_together": {("data_register", "name_producction")},
            },
        ),
    ]
