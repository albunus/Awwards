# Generated by Django 3.2.9 on 2021-12-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telphone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
