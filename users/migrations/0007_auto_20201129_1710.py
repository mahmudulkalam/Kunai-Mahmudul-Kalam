# Generated by Django 3.1.3 on 2020-11-29 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201129_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='fcm_token',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fcm_token',
        ),
    ]
