import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from .models import Developer


# Create your views here.

def index(request):
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('name')
    })


def watchlist(request):
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all().order_by('name')
    })


def addDeveloper(request):
    d = Developer(name=request.GET["name"])
    d.save()
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all().order_by('name')
    })


def deleteDeveloper(request):
    d = Developer.objects.filter(name__contains=request.GET["name"])
    d.delete()
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all().order_by('name')
    })


def nobetcify(request):
    Developer.objects.all().update(isNobetci=False)
    Developer.objects.filter(name__contains=request.GET["name"]).update(isNobetci=True)
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all().order_by('name')
    })


def health(request):
    return HttpResponse(PageView.objects.count())
