# Generated by Django 5.0.7 on 2024-08-09 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0025_remove_files_commission_commission_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.plants', verbose_name='Станция'),
        ),
    ]
