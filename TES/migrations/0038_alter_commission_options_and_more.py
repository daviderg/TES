# Generated by Django 5.0.7 on 2024-08-16 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0037_alter_employer_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commission',
            options={'verbose_name': 'Комиссия', 'verbose_name_plural': 'Комиссии'},
        ),
        migrations.AlterModelOptions(
            name='commissiontype',
            options={'verbose_name': 'Тип комиссии', 'verbose_name_plural': 'Типы комиссий'},
        ),
        migrations.AlterModelOptions(
            name='employer',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AddField(
            model_name='commission',
            name='leader',
            field=models.CharField(default='Лидер', max_length=255, unique=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='commission',
            name='commission_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.commissiontype', verbose_name='Тип комиссии'),
        ),
        migrations.AlterField(
            model_name='commission',
            name='lvl',
            field=models.CharField(max_length=255, verbose_name='Уровень комиссии'),
        ),
        migrations.AlterField(
            model_name='commissiontype',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тип комиссии'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='commission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.commission', verbose_name='Комиссия'),
        ),
    ]
