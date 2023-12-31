# Generated by Django 4.2.5 on 2023-10-24 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0026_remove_logs_period_alter_mailing_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Тема рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 9, 15, 33, 646135), verbose_name='Время начала'),
        ),
    ]
