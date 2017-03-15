import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from .models import Developer
from .models import Audit
import datetime
from ipware.ip import get_ip
from django.core.mail import send_mail


# Create your views here.

def index(request):
    developers = Developer.objects.all().order_by('date')
    ipstr = get_ip(request)
    if ipstr is not None:
        audit, created = Audit.objects.get_or_create(ip=ipstr)
        audit.lastvisit = datetime.datetime.now()
        if not created:
            audit.count += 1
            audit.save()
    for dev in developers:
        if dev.date == datetime.datetime.today().date():
            dev.isNobetci=True
    return render(request, 'welcome/index.html', {
        'developers': developers
    })

def audit(request):
    return render(request, 'welcome/audit.html', {
        'audit': Audit.objects.all().order_by('count')
    })

def sendMail(request):
    send_mail('kk-test', 'test body of the message', 'testnobetci@thy.com', ['kkarakaya@thy.com'])
    return render(request, 'welcome/audit.html', {
        'audit': Audit.objects.all().order_by('count')
    })

class DevDate(object):
    developer = Developer()
    date = datetime.date

    # The class "constructor" - It's actually an initializer
    def __init__(self, developer, date):
        self.developer = developer
        self.date = date

def addDeveloper(request):
    mDate = datetime.datetime.strptime(request.GET["date"], '%d%m%y').date()
    d = Developer(name=request.GET["name"], date=mDate)
    d.save()
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('date')
    })

def deleteDeveloper(request):
    mDate = datetime.datetime.strptime(request.GET["date"], '%d%m%y').date()
    d = Developer.objects.filter(name__exact=request.GET["name"]).filter(date__exact=mDate)
    d.delete()
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('date')
    })


def nobetcify(request):
    Developer.objects.all().update(isNobetci=False)
    Developer.objects.filter(name__exact=request.GET["name"]).update(isNobetci=True)
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('date')
    })


def health(request):
    return HttpResponse(PageView.objects.count())
