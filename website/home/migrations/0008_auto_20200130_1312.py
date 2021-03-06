# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-30 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200127_0653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allprogramming',
            options={'verbose_name_plural': 'Master Program'},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ('-date',), 'verbose_name_plural': 'Z program'},
        ),
        migrations.AlterModelOptions(
            name='subprogramming',
            options={'verbose_name_plural': 'sub program'},
        ),
        migrations.AlterField(
            model_name='allprogramming',
            name='Allprog_slug',
            field=models.SlugField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='program',
            name='lecture_slug',
            field=models.SlugField(default=1, max_length=200),
        ),
    ]
