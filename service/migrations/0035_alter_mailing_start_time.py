# Generated by Django 4.2.5 on 2023-10-30 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0034_alter_mailing_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 30, 14, 32, 21, 874584), verbose_name='Время начала'),
        ),
    ]
