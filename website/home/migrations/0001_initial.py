# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-22 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('video', models.TextField()),
                ('explain', models.TextField()),
            ],
        ),
    ]