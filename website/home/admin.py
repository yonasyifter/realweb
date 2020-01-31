# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Allprogramming, SubProgramming, Program

# Register your models here.
class allProgAdmin(admin.ModelAdmin):
    fieldsets = [('URL', {'fields': ['Allprog_slug']}), ('Photo describe of the Programming or Course', {'fields': ['img']}), ('The content of the course', {'fields': ['course', 'description']})]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = ('course', 'description')
class subProgAdmin(admin.ModelAdmin):
    fieldsets = [('Image that describe the course', {'fields': ['sub_img']}),('some Description', {'fields': ['sub_programming', 'sub_course', 'sub_description']})]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
class progAdmin(admin.ModelAdmin):
    fieldsets = [('Lecture URL', {'fields': ['lecture_slug']}), ('programming Language', {'fields': ['Programming']}), ('Title and Date', {'fields': ['title', 'date']}), ('Content Block', {'fields': ['explain']})]
    formfield_overrides = {
                models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Allprogramming, allProgAdmin)
admin.site.register(SubProgramming, subProgAdmin)
admin.site.register(Program, progAdmin)
