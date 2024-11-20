# Generated by Django 5.0.3 on 2024-03-12 04:36

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0020_alter_client_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "مشتری", "verbose_name_plural": "مشتریان"},
        ),
        migrations.RemoveField(
            model_name="product",
            name="pcategory",
        ),
        migrations.AddField(
            model_name="product",
            name="pcategory",
            field=models.SlugField(default=0, verbose_name=shop.models.category),
            preserve_default=False,
        ),
    ]
