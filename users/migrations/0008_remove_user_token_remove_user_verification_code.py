# Generated by Django 4.2.5 on 2023-10-31 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_verification_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verification_code',
        ),
    ]
