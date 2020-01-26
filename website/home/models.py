# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Allprogramming(models.Model):
    course = models.CharField(max_length=200)
    img = models.TextField(default='0')
    description = models.CharField(max_length=400)
    def __str__(self):
        return self.course

class Program(models.Model):
    Programming = models.ForeignKey(Allprogramming, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    video = models.TextField()
    explain = models.TextField()

def __str__(self):
    return title
