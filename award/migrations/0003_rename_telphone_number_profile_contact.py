# Generated by Django 3.2.9 on 2021-12-10 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_profile_telphone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='telphone_number',
            new_name='contact',
        ),
    ]
