# Generated by Django 5.1 on 2024-09-15 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occupancy', '0002_roomoccupancy_sensor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomoccupancy',
            name='temperature',
        ),
    ]