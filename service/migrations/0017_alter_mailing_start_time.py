# Generated by Django 4.2.5 on 2023-10-22 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_alter_mailing_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 22, 21, 33, 32, 599105), verbose_name='Время начала'),
        ),
    ]
