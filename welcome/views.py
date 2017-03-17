import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from .models import Developer
from .models import Audit
from .models import Meta
import datetime
from ipware.ip import get_ip
from django.core.mail import send_mail
from django.core.mail import EmailMessage


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
            dev.isNobetci = True
    return render(request, 'welcome/index.html', {
        'developers': developers,
        'ipstr': ipstr
    })


def audit(request):
    return render(request, 'welcome/audit.html', {
        'audit': Audit.objects.all().order_by('count')
    })


def sendMail(request):
    senderDefaultEmail = os.environ.get('EMAIL_SENDER')
    teamEmail = os.environ.get('TEAM_EMAIL')
    branch = request.POST["branch"]
    ortam = ""
    if 'ortam1' in request.POST:
        ortam += request.POST['ortam1'] + ", "
    if 'ortam2' in request.POST:
        ortam += request.POST['ortam2'] + ", "
    if 'ortam3' in request.POST:
        ortam += request.POST['ortam3'] + ", "
    if 'ortam4' in request.POST:
        ortam += request.POST['ortam4'] + ", "
    if 'ortam5' in request.POST:
        ortam += request.POST['ortam5'] + ", "
    if 'ortam6' in request.POST:
        ortam += request.POST['ortam6'] + ", "
    if 'ortam7' in request.POST:
        ortam += request.POST['ortam7'] + ", "
    if 'ortam8' in request.POST:
        ortam += request.POST['ortam8']
    if ortam.endswith(", "):
        ortam = ortam[:-2]
    nobetciName = request.POST['nobetci']
    senderIp = request.POST['sender']

    try:
        nobetci = Meta.objects.all().filter(name__exact=nobetciName).get()
    except Meta.DoesNotExist:
        nobetci = None
    if nobetci is not None:
        nobetciMail = nobetci.email
    try:
        sender = Meta.objects.all().filter(ipaddress__exact=senderIp).get()
    except Meta.DoesNotExist:
        sender = None
    body = 'merhaba ' + nobetciName + ', \n\n ' + branch + '\'dan ' + ortam + '\'a deployment yapabilir misin? \n\n tesekkurler.\n'
    senderMail = " "
    nobetciMail = " "
    if sender is not None:
        body += sender.name
        senderMail = sender.email
    if senderMail is " ":
        senderMail = senderDefaultEmail
    if nobetciMail is " ":
        nobetciMail = teamEmail
    # send_mail('nobetci: deployment talebi', body, senderMail, nobetciMail)
    email = EmailMessage(subject='nobetci: deployment talebi', body=body, from_email=senderMail, to=[nobetciMail],cc=teamEmail)
    email.send()
    return render(request, 'welcome/emailSent.html', {
        'body': body
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

def addMeta(request):
    d = Meta(name=request.GET["name"], email=request.GET["email"], ipaddress=request.GET["ip"])
    d.save()
    return render(request, 'welcome/meta.html', {
        'meta': Meta.objects.all().order_by('name')
    })

def deleteMeta(request):
    d = Meta.objects.filter(name__exact=request.GET["name"])
    d.delete()
    return render(request, 'welcome/meta.html', {
        'meta': Meta.objects.all().order_by('name')
    })

def nobetcify(request):
    Developer.objects.all().update(isNobetci=False)
    Developer.objects.filter(name__exact=request.GET["name"]).update(isNobetci=True)
    return render(request, 'welcome/index.html', {
        'developers': Developer.objects.all().order_by('date')
    })


def health(request):
    return HttpResponse(PageView.objects.count())
