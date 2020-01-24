# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Program

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def electronics(request):
    return render(request, 'home/electronics.html')

def program(request):

    return render(request, 'home/programming.html')


def projects(request):
    return render(request, 'home/projects.html')

def about_me(request):
    return render(request, 'home/about_me.html')

def python(request, python_id):
    python_id = Program.objects.all(pk=python_id)
    python = Program.objects.all()
    context = {
            'python': python, 'python_id': python_id
        }
    return render(request, 'home/program/python.html', context)
