# Generated by Django 5.0.7 on 2024-08-05 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0023_employer_exam_alter_score_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='экзамен', to='TES.exam', verbose_name='Тип экзамена'),
        ),
    ]
