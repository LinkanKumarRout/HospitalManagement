# Generated by Django 3.2.18 on 2023-05-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0009_alter_allappointments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allappointments',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
