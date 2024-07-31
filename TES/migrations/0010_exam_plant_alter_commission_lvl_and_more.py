# Generated by Django 5.0.7 on 2024-07-29 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0009_plants_description_plants_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.plants', verbose_name='Станция'),
        ),
        migrations.AlterField(
            model_name='commission',
            name='lvl',
            field=models.CharField(max_length=255, verbose_name='Уровень камиссии'),
        ),
        migrations.AlterField(
            model_name='commission',
            name='user_name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]