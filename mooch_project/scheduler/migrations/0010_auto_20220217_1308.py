# Generated by Django 3.2.9 on 2022-02-17 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20220217_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtime',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 17, 13, 8, 45, 477187), null=True),
        ),
        migrations.AlterField(
            model_name='runtime',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 17, 13, 8, 45, 477187), null=True),
        ),
    ]
