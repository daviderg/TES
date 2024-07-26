# Generated by Django 5.0.7 on 2024-07-24 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0007_remove_employer_category_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='commission_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.commissiontype', verbose_name='Тип коммиссии'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.plants', verbose_name='Станция'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='files',
            name='commission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TES.commission', verbose_name='Камиссия'),
        ),
        migrations.AlterField(
            model_name='files',
            name='files',
            field=models.FileField(null=True, upload_to='files/', verbose_name='Файл'),
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
            model_name='user',
            name='role',
            field=models.ManyToManyField(related_name='users', to='TES.userrole', verbose_name='Роль'),
        ),
    ]
