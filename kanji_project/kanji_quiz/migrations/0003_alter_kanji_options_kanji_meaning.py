# Generated by Django 4.0.1 on 2022-02-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_quiz', '0002_alter_kanji_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kanji',
            options={'verbose_name_plural': 'Kanji'},
        ),
        migrations.AddField(
            model_name='kanji',
            name='meaning',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
