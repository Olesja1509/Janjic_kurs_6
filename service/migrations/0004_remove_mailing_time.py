# Generated by Django 4.2.5 on 2023-10-13 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_mailing_finish_time_mailing_start_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='time',
        ),
    ]
