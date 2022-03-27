# Generated by Django 3.2.9 on 2022-03-01 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20220301_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='runtime',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 9, 33, 52, 396710), null=True),
        ),
        migrations.AlterField(
            model_name='runtime',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 1, 9, 33, 52, 396710), null=True),
        ),
    ]