# Generated by Django 4.2.4 on 2024-02-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_mahsool_is_special_mahsool_special_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsool',
            name='is_special',
            field=models.BooleanField(null=True, verbose_name='فروش ویژه'),
        ),
    ]