from django.conf.urls import url
from . import views
from .models import Program

# app_name = home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^electronics/$', views.electronics, name='electronics'),
    url(r'^programming/$', views.program, name='program'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'^python/$', views.python,  name='python'),

]
