#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext , Context
from django.views.decorators.csrf import *
from django.core import serializers #serualizer
import os, sys
import time, subprocess, datetime
import hashlib, json
import Leap, gao


@csrf_exempt
def hack(request):
	return render_to_response("hack.html")


@csrf_exempt
def getLeapData(request):
	data = gao.getLeapData()

	ret = json.dumps(data)
	response = HttpResponse()
	response['Content-Type'] = 'text/javascript'
	response.write(ret)
	return response
