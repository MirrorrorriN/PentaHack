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
	datas, data = gao.getLeapData(), {}
	flag, suc = False, False
	hand = []

	for each in datas:
		if len(each['gesture']):
			if each['gesture'][0]['type'] == 'keytap' or each['gesture'][0]['type'] == 'screentap':
				data, suc = each, True #说明有正确gesture
				break
			else:
				data = each
		elif len(each['hand']):
			hand = each['hand']
			flag = True #说明有用leap

	if flag and not suc:
		data = {'hand':hand, 'gesture':[]}

	#print data

	ret = json.dumps(data)
	print ret

	response = HttpResponse()
	response['Content-Type'] = 'text/javascript'
	response.write(ret)
	return response


@csrf_exempt
def getLeapData1(request):
	ret = {'status':'ok'}
	ret = json.dumps(ret)
	print ret
	response = HttpResponse()
	response['Content-Type'] = 'text/javascript'
	response.write(ret)
	return response
