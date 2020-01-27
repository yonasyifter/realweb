# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Allprogramming, SubProgramming, Program

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def electronics(request):
    return render(request, 'home/electronics.html')

def program(request):
    allprog = Allprogramming.objects.all()
    context = {
        'allprog': allprog
    }
    return render(request, 'home/programming.html', context)

def slug_request(request, slug_request):
        allProg = [a.Allprog_slug for a in Allprogramming.objects.all()]
        if slug_request in allProg:
            matching_sites = SubProgramming.objects.filter(sub_programming__Allprog_slug=slug_request)
            allSeries = {}
            for m in matching_sites:
                lecture = Program.objects.filter(Programming__sub_course=m.sub_course).earliest('published date')
                allSeries[m] = lecture.lecture_slug
            context = {
                'allSeries': allSeries
            }
            return render(request, 'home/subprog.html', context)

        lecture = [l.lecture_slug for l in Program.objects.all()]
        if slug_request in lecture:
            




def projects(request):
    return render(request, 'home/projects.html')

def about_me(request):
    return render(request, 'home/about_me.html')
