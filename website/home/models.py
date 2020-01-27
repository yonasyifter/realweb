# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Allprogramming(models.Model):
    course = models.CharField(max_length=200)
    img = models.TextField(default='0')
    description = models.CharField(max_length=400)
    Allprog_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = 'Allprogram'

    def __str__(self):
        return self.course

class SubProgramming(models.Model):
    sub_programming = models.ForeignKey(Allprogramming, default=1, verbose_name='Allprogram', on_delete=models.SET_DEFAULT)
    sub_course = models.CharField(max_length=200)
    sub_img = models.TextField()
    sub_description = models.CharField(max_length=400)
    class Meta:
        verbose_name_plural = 'subProg'
    def __str__(self):
        return self.sub_course

class Program(models.Model):
    Programming = models.ForeignKey(SubProgramming, default=1, verbose_name='subProg', on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    date = models.DateTimeField('Date Published')
    explain = models.TextField()
    lecture_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.title
