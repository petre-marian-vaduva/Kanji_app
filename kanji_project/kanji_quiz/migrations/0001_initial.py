# Generated by Django 4.0.1 on 2022-02-03 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kanji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=20)),
                ('level', models.IntegerField(max_length=1)),
                ('is_number', models.BooleanField()),
                ('is_radical', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Portuguese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation', models.CharField(max_length=100)),
                ('example', models.TextField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanji_quiz.kanji')),
            ],
        ),
    ]
