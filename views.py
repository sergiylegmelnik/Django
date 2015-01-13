# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.db import connection
# from models import Book
import datetime

# def book_list(request):
#     books = Book.objects.order_by('name')
#     return render_to_response('book_list.html', {'books': books})


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def home(request):
    cursor = connection.cursor()
    return HttpResponse(u"Home view")