# Generated by Django 4.0.1 on 2022-02-03 23:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_quiz', '0004_alter_portuguese_options_remove_kanji_meaning_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanji',
            name='level',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
