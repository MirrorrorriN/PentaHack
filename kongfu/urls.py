from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from kongfu.views import *

urlpatterns = patterns('',
	url(r'^hack', hack),
	url(r'^getLeapData', getLeapData),
)