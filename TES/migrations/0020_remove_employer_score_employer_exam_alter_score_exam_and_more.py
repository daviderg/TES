# Generated by Django 5.0.7 on 2024-08-05 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0019_employer_score_alter_score_exam_alter_score_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='score',
        ),
        migrations.AddField(
            model_name='employer',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.exam', verbose_name='Тип экзамена'),
        ),
        migrations.AlterField(
            model_name='score',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.exam', verbose_name='Тип экзамена'),
        ),
        migrations.AlterField(
            model_name='score',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.employer', verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
