# Generated by Django 4.2.5 on 2023-10-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_mailing_is_active_alter_mailing_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Отметка об активности'),
        ),
    ]
