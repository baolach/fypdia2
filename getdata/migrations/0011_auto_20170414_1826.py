# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0010_auto_20170414_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getlocation',
            old_name='coordinates',
            new_name='location_name',
        ),
        migrations.RenameField(
            model_name='getlocation',
            old_name='type',
            new_name='location_type',
        ),
        migrations.RemoveField(
            model_name='getlocation',
            name='x',
        ),
        migrations.RemoveField(
            model_name='getlocation',
            name='y',
        ),
        migrations.AddField(
            model_name='getlocation',
            name='location_x',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='getlocation',
            name='location_y',
            field=models.IntegerField(default=None),
        ),
    ]