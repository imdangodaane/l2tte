# Generated by Django 2.2.7 on 2019-11-28 16:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191128_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='is_authenticated',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 28, 16, 33, 23, 970904, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='expired_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 28, 16, 48, 23, 970928, tzinfo=utc), null=True),
        ),
    ]
