# Generated by Django 3.1.3 on 2020-11-23 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201120_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
            preserve_default=False,
        ),
    ]
