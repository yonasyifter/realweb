# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Program, Allprogramming

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


def projects(request):
    return render(request, 'home/projects.html')

def about_me(request):
    return render(request, 'home/about_me.html')

def python(request):
    python = Program.objects.all()
    context = {
            'python': python
        }
    return render(request, 'home/program/python.html', context)
