# Generated by Django 3.1.3 on 2020-11-14 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leaves', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavereportstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='leavereportstaff',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.staff'),
        ),
    ]