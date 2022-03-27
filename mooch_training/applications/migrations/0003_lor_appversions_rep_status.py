# Generated by Django 3.2.9 on 2022-02-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_alter_ipm_appversions_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lor_appversions',
            name='Rep_Status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1, null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
    ]