from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from kongfu.views import *

urlpatterns = patterns('',
	url(r'^index/', hack),
	url(r'^getLeapData/', getLeapData),
)