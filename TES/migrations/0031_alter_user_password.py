# Generated by Django 5.0.7 on 2024-08-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0030_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='TES123456789', max_length=255, verbose_name='Пароль'),
        ),
    ]