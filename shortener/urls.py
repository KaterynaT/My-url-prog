from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', 'shortener.views.home', name='home'),
    url(r'^(?P<id>[a-zA-Z0-9]+)/$', 'shortener.views.link'),    
]