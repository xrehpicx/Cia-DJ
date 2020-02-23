# Generated by Django 2.0.10 on 2020-02-04 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200204_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='u_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='attendregister',
            name='a_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 4, 18, 4, 8, 980223)),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 4, 18, 4, 8, 981630)),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 4, 18, 4, 8, 983228)),
        ),
    ]
