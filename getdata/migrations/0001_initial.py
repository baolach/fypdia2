# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.TextField(default=None)),
                ('client_phone', models.CharField(default=None, max_length=10)),
                ('client_address', models.TextField(default=None)),
                ('log_no', models.TextField(default=None)),
                ('driver_no', models.TextField(default=None)),
                ('dob', models.TextField(default=None)),
                ('no_of_lessons', models.CharField(default=None, max_length=10)),
                ('balance_due', models.CharField(default=None, max_length=3)),
                ('comments', models.TextField(default=None)),
            ],
        ),
    ]