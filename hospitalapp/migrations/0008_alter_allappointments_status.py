# Generated by Django 3.2.18 on 2023-05-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0007_allappointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allappointments',
            name='status',
            field=models.IntegerField(max_length=10),
        ),
    ]