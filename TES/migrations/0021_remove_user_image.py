# Generated by Django 5.0.7 on 2024-08-05 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TES', '0020_remove_employer_score_employer_exam_alter_score_exam_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
