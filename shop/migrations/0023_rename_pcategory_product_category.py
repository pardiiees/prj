# Generated by Django 5.0.3 on 2024-03-12 04:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0022_remove_product_pcategory_product_pcategory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="pcategory",
            new_name="category",
        ),
    ]
