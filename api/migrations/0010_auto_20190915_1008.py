# Generated by Django 2.2.5 on 2019-09-15 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190915_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 15, 10, 8, 27, 987548)),
        ),
    ]
