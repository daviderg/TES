# Generated by Django 5.0.7 on 2024-08-09 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0026_user_plant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='plant',
        ),
    ]
