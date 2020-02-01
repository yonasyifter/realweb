from django.conf.urls import url
from . import views
from .models import Allprogramming, SubProgramming, Program

# app_name = home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^all_program/$', views.all_program, name='all_program'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'all_program/(?P<slug_request>[-\w]+)/$', views.slug_request, name='slug_request'),


]
