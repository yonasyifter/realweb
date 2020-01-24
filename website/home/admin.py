# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Program

# Register your models here.
class progAdmin(admin.ModelAdmin):
    fieldsets = [('Title and Date',{'fields':['title','date']}),
                 ('Content Block',{'fields':['video','explain']})]
    formfield_overrides = {
                models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Program, progAdmin)
