# Generated by Django 4.0.3 on 2023-04-08 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_orders_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='plates',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orders',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 8, 14, 11, 32, 763)),
        ),
    ]