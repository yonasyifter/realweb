# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-30 16:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200130_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 32, 30, 352515, tzinfo=utc), verbose_name='Date Published'),
        ),
    ]