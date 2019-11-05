# Generated by Django 2.0.10 on 2019-11-05 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20191028_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='visioneer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='firstname', max_length=100)),
                ('lastname', models.CharField(default='lastname', max_length=100)),
                ('emailaddress', models.EmailField(default='emailaddress', max_length=100)),
                ('password', models.CharField(default='password', max_length=100)),
                ('passwordhashfunction', models.CharField(default='title', max_length=100)),
                ('orgunitpath', models.CharField(default='title', max_length=100)),
                ('newprimaryemail', models.EmailField(default='title', max_length=100)),
                ('recoveryemail', models.EmailField(default='title', max_length=100)),
                ('hsecondaryemail', models.EmailField(default='title', max_length=100)),
                ('wsecondaryemail', models.EmailField(default='title', max_length=100)),
                ('rphone', models.CharField(default='title', max_length=13)),
                ('wphone', models.CharField(default='title', max_length=13)),
                ('hphone', models.CharField(default='title', max_length=13)),
                ('mphone', models.CharField(default='title', max_length=13)),
                ('workaddress', models.CharField(default='title', max_length=100)),
                ('homeaddress', models.CharField(default='title', max_length=100)),
                ('employeeid', models.CharField(default='title', max_length=100)),
                ('employeetype', models.CharField(default='title', max_length=100)),
                ('employeetitle', models.CharField(default='title', max_length=100)),
                ('manageremail', models.EmailField(default='title', max_length=100)),
                ('departement', models.CharField(default='title', max_length=100)),
                ('costcenter', models.CharField(default='title', max_length=100)),
                ('buildingid', models.CharField(default='title', max_length=100)),
                ('floorname', models.CharField(default='title', max_length=100)),
                ('floorsection', models.CharField(default='title', max_length=100)),
                ('changepasswordatnextsignin', models.CharField(default='title', max_length=100)),
                ('newstatus', models.CharField(default='title', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='attendregister',
            name='a_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 3, 48, 43, 903827)),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 3, 48, 43, 905123)),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 5, 3, 48, 43, 906695)),
        ),
    ]