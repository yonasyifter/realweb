# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Program, Allprogramming

# Register your models here.
class progAdmin(admin.ModelAdmin):
    fieldsets = [('programming Language', {'fields': ['Programming']}), ('Title and Date', {'fields': ['title', 'date']}), ('Content Block', {'fields': ['video', 'explain']})]
    formfield_overrides = {
                models.TextField: {'widget': TinyMCE()},
        }
class allProgAdmin(admin.ModelAdmin):
    fieldsets = [('Photo describe of the Programming or Course', {'fields': ['img']}), ('The content of the course', {'fields': ['course', 'description']})]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Program, progAdmin)
admin.site.register(Allprogramming, allProgAdmin)
