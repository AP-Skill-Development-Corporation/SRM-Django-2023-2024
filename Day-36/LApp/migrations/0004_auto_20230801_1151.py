# Generated by Django 3.0 on 2023-08-01 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LApp', '0003_auto_20230801_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='tchdescc',
            new_name='tchdesc',
        ),
    ]
