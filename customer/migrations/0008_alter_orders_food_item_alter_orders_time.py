# Generated by Django 4.0.3 on 2022-03-29 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_remove_orders_price_orders_status_alter_orders_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='food_item',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 17, 55, 44, 533771)),
        ),
    ]
