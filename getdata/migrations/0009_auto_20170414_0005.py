# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0008_auto_20170413_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.TextField(default=None)),
                ('expense_amount', models.CharField(default=None, max_length=6)),
                ('expense_date', models.DateField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='getlocation',
            name='x',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='getlocation',
            name='y',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
