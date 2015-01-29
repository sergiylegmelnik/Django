# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect
from django.db import connection
from presistence.models import Publisher, Book
from presistence.models import Item
import datetime

# def book_list(request):
#     books = Book.objects.order_by('name')
#     return render_to_response('book_list.html', {'books': books})


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


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


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def home(request):
    if request.method == 'POST':
        item = Item()
        item.text = request.POST.get('item_text', '')
        item.save()
        return redirect('/')

    items = Item.objects.all()
    model = {'title': 'To-Do', 'items': items}

    return render_to_response('home.html', model, RequestContext(request))
