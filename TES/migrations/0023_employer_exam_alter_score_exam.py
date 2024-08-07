# Generated by Django 5.0.7 on 2024-08-05 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0022_remove_employer_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.exam', verbose_name='Тип экзамена'),
        ),
        migrations.AlterField(
            model_name='score',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='экзамен', to='TES.employer', verbose_name='Тип экзамена'),
        ),
    ]
