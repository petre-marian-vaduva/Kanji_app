# Generated by Django 3.2.9 on 2022-02-21 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0012_auto_20220221_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtime',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 15, 22, 59, 342426), null=True),
        ),
        migrations.AlterField(
            model_name='runtime',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 15, 22, 59, 342426), null=True),
        ),
    ]
