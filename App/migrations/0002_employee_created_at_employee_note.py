# Generated by Django 4.2.1 on 2023-05-27 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 5, 27, 11, 55, 40, 74963, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='note',
            field=models.TextField(default=datetime.datetime(2023, 5, 27, 11, 56, 5, 603791, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
