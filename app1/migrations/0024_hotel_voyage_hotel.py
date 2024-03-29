# Generated by Django 4.2.7 on 2024-01-06 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_vol_titre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(max_length=100)),
                ('nbr_etoiles', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])),
                ('nbr_chambres', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='voyage',
            name='hotel',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='app1.hotel'),
        ),
    ]
