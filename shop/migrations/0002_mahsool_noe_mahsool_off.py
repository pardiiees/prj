# Generated by Django 4.2.4 on 2023-08-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsool',
            name='noe',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='mahsool',
            name='off',
            field=models.IntegerField(default=1),
        ),
    ]
