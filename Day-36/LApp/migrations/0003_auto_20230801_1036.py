# Generated by Django 3.0 on 2023-08-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LApp', '0002_auto_20230731_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='stprofile',
            name='sstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tchprofile',
            name='tstatus',
            field=models.BooleanField(default=False),
        ),
    ]
