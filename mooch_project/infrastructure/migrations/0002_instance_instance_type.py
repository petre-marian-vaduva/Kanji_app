# Generated by Django 4.0.1 on 2022-02-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='Instance_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
