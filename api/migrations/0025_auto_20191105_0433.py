# Generated by Django 2.0.10 on 2019-11-05 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20191105_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendregister',
            name='a_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 4, 33, 19, 398112)),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 4, 33, 19, 398970)),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 4, 33, 19, 400009)),
        ),
        migrations.AlterField(
            model_name='visioneer',
            name='emailaddress',
            field=models.EmailField(default='emailaddress', max_length=100, unique=True),
        ),
    ]
