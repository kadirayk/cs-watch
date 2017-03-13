import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from .models import Developer

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def watchlist(request):
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all()
    })

def addDeveloper(request):
    d = Developer(name=request.GET["name"])
    d.save()
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all()
    })

def deleteDeveloper(request):
    d = Developer.objects.filter(name__contains=request.GET["name"])
    d.delete()
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all()
    })

def nobetcify(request):
    Developer.objects.filter(name__contains=request.GET["name"]).update(isNobetci=True)
    return render(request, 'welcome/watchlist.html', {
        'developers': Developer.objects.all()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
