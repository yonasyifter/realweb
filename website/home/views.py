# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Allprogramming, SubProgramming, Program

def home(request):
    return render(request, 'home/home.html')


def all_program(request):
    allprog = Allprogramming.objects.all()
    context = {
        'allprog': allprog
    }
    return render(request, 'home/all_program.html', context)

def slug_request(request, slug_request):
    allProg = [a.Allprog_slug for a in Allprogramming.objects.all()]
    if slug_request in allProg:
        matching_sites = SubProgramming.objects.filter(sub_programming__Allprog_slug=slug_request)
        allSeries = {}
        for m in matching_sites.all():
            lecture = Program.objects.filter(Programming__sub_course=m.sub_course)
            allSeries[m] = lecture
    return render(request, 'home/subprog.html', context={'allSeries': allSeries })
#
#
# lecture starts here
    lectur = [l.lecture_slug for l in Program.objects.all()]
    if slug_request in lectur:
        this_lecture = Program.objects.all(lecture_slug=slug_request)
        context = {'tutorial': this_lecture}
    return render(request, 'home/lecture.html', context)


def about_me(request):
    return render(request, 'home/about_me.html')
