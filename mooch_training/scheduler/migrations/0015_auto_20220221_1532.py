# Generated by Django 3.2.9 on 2022-02-21 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_auto_20220221_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtime',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 15, 32, 18, 394999), null=True),
        ),
        migrations.AlterField(
            model_name='runtime',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 15, 32, 18, 394999), null=True),
        ),
    ]
