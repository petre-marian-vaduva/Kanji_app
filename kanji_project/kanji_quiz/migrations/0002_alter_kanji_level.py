# Generated by Django 4.0.1 on 2022-02-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanji',
            name='level',
            field=models.IntegerField(),
        ),
    ]
