from django.conf.urls import url
from . import views
from .models import Allprogramming, SubProgramming, Program

# app_name = home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^electronics/$', views.electronics, name='electronics'),
    url(r'^programming/$', views.programming, name='programming'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^entertainment/$', views.projects, name='entertainment'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'^<slug_request>/$', views.slug_request, name='slug_request'),
]
