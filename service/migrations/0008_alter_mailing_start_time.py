# Generated by Django 4.2.5 on 2023-10-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_mailing_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Время начала'),
        ),
    ]
