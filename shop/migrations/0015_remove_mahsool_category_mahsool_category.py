# Generated by Django 4.2.4 on 2024-02-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahsool',
            name='category',
        ),
        migrations.AddField(
            model_name='mahsool',
            name='category',
            field=models.ManyToManyField(to='shop.category'),
        ),
    ]