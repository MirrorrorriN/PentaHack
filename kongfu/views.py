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
import Leap


@csrf_exempt
def hack(request):
	return render_to_response("hack.html")