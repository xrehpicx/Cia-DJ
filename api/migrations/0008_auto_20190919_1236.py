# Generated by Django 2.0.13 on 2019-09-19 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190919_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 19, 12, 36, 52, 264543)),
        ),
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]