# Generated by Django 3.1.3 on 2020-11-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='students/'),
            preserve_default=False,
        ),
    ]
