# Generated by Django 3.2.9 on 2022-03-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_quiz', '0006_alter_kanji_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='kanji',
            name='example',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kanji',
            name='meaning',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='kanji',
            name='character',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
