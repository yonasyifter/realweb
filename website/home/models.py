# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Program(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    video = models.TextField()
    explain = models.TextField()

def __str__(self):
    return title
