# Generated by Django 2.2.7 on 2019-11-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191119_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='group_id',
            field=models.IntegerField(default=0),
        ),
    ]
