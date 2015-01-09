# -*- coding: utf-8 -*-
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello view")

def home(request):
    return HttpResponse("Home view")