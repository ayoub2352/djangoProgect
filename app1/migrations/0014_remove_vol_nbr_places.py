# Generated by Django 4.2.7 on 2024-01-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_vol_nbr_places_alter_vol_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vol',
            name='nbr_places',
        ),
    ]